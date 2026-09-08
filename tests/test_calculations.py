from pathlib import Path
import sys,json,unittest,tempfile,math
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from calculate import calculate,load_rows,ROOT
from prepare_femm import prepare

class EngineeringChecks(unittest.TestCase):
    def setUp(self):
        self.p=json.loads((ROOT/'calculations/parameters.json').read_text())
        self.rows=load_rows(ROOT/'simulation/rev64/Rev64_CENTERED_COIL_PM_KF.csv')
        self.old=load_rows(ROOT/'archive/recovered-history/Rev62_CENTERED_COIL_PM_KF.csv')
    def calc(self): return calculate(self.p,self.rows,self.old)
    def test_independent_winding_clearance(self):
        r=self.calc()
        self.assertAlmostEqual(r['radial_allowance_mm'],0.014)
        self.assertAlmostEqual(r['axial_allowance_mm'],0.066)
        self.assertAlmostEqual(r['coil_end_margin_at_full_travel_mm'],5)
    def test_too_thick_wire_rejected(self):
        self.p['finished_wire_mm']=0.29
        with self.assertRaises(ValueError): self.calc()
    def test_bad_turn_count_rejected(self):
        self.p['layer_turns']=[14]*6
        with self.assertRaises(ValueError): self.calc()
    def test_excess_travel_rejected(self):
        self.p['travel_half_mm']=25
        with self.assertRaises(ValueError): self.calc()
    def test_leads_affect_resistance_not_packing(self):
        r1=self.calc(); self.p['extra_wire_per_coil_m']+=1; r2=self.calc()
        self.assertAlmostEqual(r2['coil_resistance20_ohm']-r1['coil_resistance20_ohm'],0.3482)
        self.assertEqual(r1['radial_allowance_mm'],r2['radial_allowance_mm'])
    def test_gravity_load(self):
        r=self.calc()
        self.assertAlmostEqual(r['historical_vertical_upward_force_no_friction_N']-r['historical_horizontal_inertia_force_N'],0.5*9.80665)
    def test_current_normalization_and_loss(self):
        r=self.calc(); u=[self.rows[80][k] for k in ['IA_norm','IB_norm','IC_norm']]
        i=[math.sqrt(1.5)*v for v in u]
        self.assertAlmostEqual(sum(x*x for x in i)*r['phase_resistance20_ohm'],1.5*r['phase_resistance20_ohm'],places=8)
    def test_preparation_preserves_previous_run(self):
        with tempfile.TemporaryDirectory() as temp:
            p=prepare(Path(temp)/'new-run')
            script=(p/'run_sweep.lua').read_text()
            self.assertNotIn('quit()',script)
            self.assertIn(p.as_posix()+'/',script)
            with self.assertRaises(FileExistsError): prepare(p)
    def test_cannot_prepare_inside_sources(self):
        with self.assertRaises(ValueError): prepare(ROOT/'simulation'/'forbidden-run')

if __name__=='__main__': unittest.main()
