"""Check preserved source integrity and archived numerical consistency."""
from pathlib import Path
import hashlib,json,math,re
from calculate import load_rows, calculate
ROOT=Path(__file__).resolve().parents[1]

def close(a,b,tol=1e-7):
    if not math.isclose(a,b,rel_tol=tol,abs_tol=tol):
        raise AssertionError(f'Numerical mismatch {a} != {b}')

def main():
    manifest=json.loads((ROOT/'archive/source_manifest.json').read_text())
    for e in manifest:
        f=ROOT/e['path']
        assert f.stat().st_size==e['bytes'],f'Size changed: {f}'
        assert hashlib.sha256(f.read_bytes()).hexdigest()==e['sha256'],f'Source changed: {f}'
    fingerprint=json.loads((ROOT/'simulation/rev64/Rev64_source_geometry_check.json').read_text())
    for filename,field in [('archive/recovered-history/Rev62_4mm_COILS_2.1mm_RADIAL_80T_ROBUST_BOBBIN.fem','parent_sha256'),('simulation/rev64/Rev64_CENTERED_0p5mm_BOBBIN_80T.fem','derived_sha256')]:
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==fingerprint[field]
    rows=load_rows(ROOT/'simulation/rev64/Rev64_CENTERED_COIL_PM_KF.csv')
    old=load_rows(ROOT/'archive/recovered-history/Rev62_CENTERED_COIL_PM_KF.csv')
    assert len(rows)==161
    for i,r in enumerate(rows):
        close(r['relative_position_mm'],-20+i*0.25)
        g=[r[k] for k in ['dLA_dx_Wb_per_m','dLB_dx_Wb_per_m','dLC_dx_Wb_per_m']]
        left=rows[max(0,i-1)]; right=rows[min(len(rows)-1,i+1)]
        dx=(right['relative_position_mm']-left['relative_position_mm'])/1000
        for val,key in zip(g,['lambdaA_Wb','lambdaB_Wb','lambdaC_Wb']): close(val,(right[key]-left[key])/dx,2e-7)
        mean=sum(g)/3; projected=[v-mean for v in g]
        k=math.sqrt(sum(v*v for v in projected))
        close(k,r['KF_unit_N'])
        u=[r[key] for key in ['IA_norm','IB_norm','IC_norm']]
        close(sum(u),0); close(sum(v*v for v in u),1)
        for v,p in zip(u,projected): close(v,p/k)
    summary=json.loads((ROOT/'simulation/rev64/Rev64_result_summary.json').read_text())
    close(sum(r['KF_unit_N'] for r in rows)/161,summary['Rev64_average_N_per_A'])
    close(sum(r['KF_unit_N'] for r in old)/len(old),summary['Rev62_average_N_per_A'])
    direct=load_rows(ROOT/'simulation/rev64/Rev64_PM_ODD_DIRECT_FORCE_VALIDATION.csv')
    assert [r['relative_position_mm'] for r in direct]==[-20,0,20]
    for r in direct:
        close((r['F_plus_N']-r['F_minus_N'])/2,r['F_PM_odd_N'])
        close((r['F_plus_N']+r['F_minus_N'])/2,r['F_even_N'])
        close(100*(r['F_PM_odd_N']-r['Rev64_KF_unit_N'])/r['Rev64_KF_unit_N'],r['difference_percent'])
        close(r['Rev64_KF_unit_N'],rows[int((r['relative_position_mm']+20)/0.25)]['KF_unit_N'])
    close(max(abs(r['difference_percent']) for r in direct),summary['max_direct_force_difference_percent'])
    p=json.loads((ROOT/'calculations/parameters.json').read_text())
    results=calculate(p,rows,old)
    stored=json.loads((ROOT/'calculations/results.json').read_text())
    assert results==stored,'Regenerate calculation results after changing inputs'
    geom=json.loads((ROOT/'cad/rev64/Rev64_geometry_validation.json').read_text())
    assert len(geom['components'])==31
    for c in geom['components']:
        kind=c['kind']
        if kind=='magnet': v=math.pi/4*p['magnet_od_mm']**2*p['magnet_length_mm']
        elif kind=='steel': v=math.pi/4*(p['magnet_od_mm']**2-p['pole_id_mm']**2)*p['pole_length_mm']
        elif kind=='tube': v=math.pi/4*(p['tube_od_mm']**2-p['tube_id_mm']**2)*results['stack_length_mm']
        elif kind=='coil': v=results['single_coil_envelope_volume_mm3']
        elif kind=='bobbin': v=results['bobbin_volume_mm3']
        else: raise AssertionError(f'Unexpected component kind {kind}')
        close(v,c['volume_mm3'])
    for item in geom['travel_checks']:
        close(item['coil_min_stack_end_margin_mm'],(results['stack_length_mm']-results['coil_pack_length_mm'])/2-abs(item['position_mm']))
    # Check links only in authored documentation; preserved source notes may contain original paths.
    authored=[ROOT/'README.md',ROOT/'CONTRIBUTING.md',*list((ROOT/'docs').glob('*.md')),*list((ROOT/'records').glob('*.md')),*list((ROOT/'calculations').glob('*.md'))]
    for f in authored:
        for target in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
            if target.startswith(('https://','http://','#')): continue
            assert (f.parent/target.split('#')[0]).exists(),f'Broken link {f}: {target}'
    print(f'PASS: {len(manifest)} source hashes; parent/current fingerprints; 161 flux/force rows; 3 direct-force checks; 31 analytical component volumes; generated results; authored local links.')

if __name__=='__main__': main()
