"""Reproduce Rev64 engineering estimates from explicit inputs and archived data.

Standard library only. Does not execute FEMM or modify source baselines.
"""
from pathlib import Path
import csv
import json
import math
import argparse

ROOT = Path(__file__).resolve().parents[1]

def load_rows(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        return [{k: float(v) for k, v in r.items()} for r in csv.DictReader(f)]

def calculate(p, rows, old_rows):
    positive = ['coil_count','turns_per_coil','coil_pitch_mm','coil_width_mm','bobbin_id_mm','bobbin_wall_mm','coil_od_mm','magnet_count','magnet_od_mm','magnet_length_mm','pole_length_mm','tube_id_mm','tube_od_mm','bare_wire_mm','finished_wire_mm','wire_resistance20_ohm_per_m','copper_density_g_cm3']
    for key in positive:
        if not isinstance(p[key], (int,float)) or not math.isfinite(p[key]) or p[key] <= 0:
            raise ValueError(f'{key} must be finite and positive')
    if p['extra_wire_per_coil_m'] < 0 or p['procurement_allowance_fraction'] < 0:
        raise ValueError('Wire allowances must not be negative')
    if p['travel_half_mm'] < 0:
        raise ValueError('Travel half span must not be negative')
    n = p['layer_turns']
    if not n or any(not isinstance(t,int) or t <= 0 for t in n) or sum(n) != p['turns_per_coil']:
        raise ValueError('Layer turns must be positive integers summing to turns_per_coil')
    if p['coil_count'] != 6:
        raise ValueError('Archived electromagnetic data apply to six coils only')
    d = p['finished_wire_mm']
    if d < p['bare_wire_mm']:
        raise ValueError('Finished wire cannot be smaller than bare conductor')
    cid = p['bobbin_id_mm']+2*p['bobbin_wall_mm']
    depth=(p['coil_od_mm']-cid)/2
    if depth <= 0 or p['coil_pitch_mm'] < p['coil_width_mm']:
        raise ValueError('Invalid winding envelope or pitch')
    build=len(n)*d
    axial=max(n)*d
    if build > depth+1e-12 or axial > p['coil_width_mm']+1e-12:
        raise ValueError('Ordered winding plan exceeds the nominal window')
    stack=p['magnet_count']*p['magnet_length_mm']+p['pole_count']*p['pole_length_mm']
    pack=(p['coil_count']-1)*p['coil_pitch_mm']+p['coil_width_mm']
    bobbin=pack+2*p['flange_mm']
    margin=(stack-bobbin)/2-p['travel_half_mm']
    if margin < 0:
        raise ValueError('Bobbin exceeds stack axial envelope at requested travel')
    layer_lengths=[turns*math.pi*(cid+(2*j+1)*d)/1000 for j,turns in enumerate(n)]
    winding=sum(layer_lengths)
    wire=winding+p['extra_wire_per_coil_m']
    area=math.pi*p['bare_wire_mm']**2/4
    rcoil=wire*p['wire_resistance20_ohm_per_m']
    rphase=2*rcoil
    ks=[r['KF_unit_N'] for r in rows]
    old=[r['KF_unit_N'] for r in old_rows]
    kavg=sum(ks)/len(ks)
    kmin=min(ks)
    kpk=kavg*math.sqrt(1.5)
    kpkmin=kmin*math.sqrt(1.5)
    force_horizontal=p['target_mass_kg']*p['target_acceleration_m_s2']
    force_vertical=p['target_mass_kg']*(p['target_acceleration_m_s2']+p['gravity_m_s2'])
    volume_coil=math.pi/4*(p['coil_od_mm']**2-cid**2)*p['coil_width_mm']
    vbase=math.pi/4*(cid**2-p['bobbin_id_mm']**2)*bobbin
    lands=(p['coil_count']-1)*(p['coil_pitch_mm']-p['coil_width_mm'])+2*p['flange_mm']
    vbobbin=vbase+math.pi/4*(p['coil_od_mm']**2-cid**2)*lands
    out={
        'stack_length_mm':stack,'coil_pack_length_mm':pack,'bobbin_length_mm':bobbin,
        'coil_id_mm':cid,'radial_window_mm':depth,'window_area_mm2':depth*p['coil_width_mm'],
        'coil_end_margin_at_full_travel_mm':(stack-pack)/2-p['travel_half_mm'],
        'bobbin_end_margin_at_full_travel_mm':margin,
        'magnet_to_tube_radial_gap_mm':(p['tube_id_mm']-p['magnet_od_mm'])/2,
        'tube_to_bobbin_radial_gap_mm':(p['bobbin_id_mm']-p['tube_od_mm'])/2,
        'wire_radial_build_mm':build,'wire_axial_build_mm':axial,
        'radial_allowance_mm':depth-build,'axial_allowance_mm':p['coil_width_mm']-axial,
        'finished_diameter_geometric_ceiling_mm':min(depth/len(n),p['coil_width_mm']/max(n)),
        'bare_copper_area_mm2':area,'cross_section_copper_fill_fraction':p['turns_per_coil']*area/(depth*p['coil_width_mm']),
        'layer_wire_lengths_m':layer_lengths,'winding_wire_length_per_coil_m':winding,
        'wire_length_with_allowance_per_coil_m':wire,'six_coil_wire_consumption_m':6*wire,
        'six_coil_purchase_with_waste_m':6*wire*(1+p['procurement_allowance_fraction']),
        'six_coils_plus_trial_purchase_m':7*wire*(1+p['procurement_allowance_fraction']),
        'coil_resistance20_ohm':rcoil,'coil_resistance20_low_ohm':wire*p['wire_resistance20_min_ohm_per_m'],
        'coil_resistance20_high_ohm':wire*p['wire_resistance20_max_ohm_per_m'],
        'phase_resistance20_ohm':rphase,'star_line_line_resistance20_ohm':2*rphase,
        'six_coil_copper_mass_including_allowance_g':6*wire*area*p['copper_density_g_cm3'],
        'bobbin_volume_mm3':vbobbin,'single_coil_envelope_volume_mm3':volume_coil,
        'Rev64_k_vector_mean_N_per_A':kavg,'Rev64_k_vector_min_N_per_A':kmin,
        'Rev64_k_vector_max_N_per_A':max(ks),'Rev64_k_phase_peak_equivalent_mean_N_per_A':kpk,
        'Rev64_k_phase_peak_equivalent_min_N_per_A':kpkmin,
        'Rev62_k_vector_mean_N_per_A':sum(old)/len(old),
        'mean_k_change_percent':100*(kavg/(sum(old)/len(old))-1),
        'kf_peak_to_peak_over_mean_percent':100*(max(ks)-min(ks))/kavg,
        'historical_horizontal_inertia_force_N':force_horizontal,
        'historical_vertical_upward_force_no_friction_N':force_vertical,
        'historical_horizontal_equivalent_peak_current_A':force_horizontal/kpkmin,
        'historical_vertical_equivalent_peak_current_A':force_vertical/kpkmin,
        'historical_vertical_hold_force_N':p['target_mass_kg']*p['gravity_m_s2'],
        'max_absolute_phase_back_emf_V_per_m_s':max(abs(r[k]) for r in rows for k in ['dLA_dx_Wb_per_m','dLB_dx_Wb_per_m','dLC_dx_Wb_per_m']),
        'max_absolute_line_back_emf_V_per_m_s':max(abs(r[a]-r[b]) for r in rows for a,b in [('dLA_dx_Wb_per_m','dLB_dx_Wb_per_m'),('dLB_dx_Wb_per_m','dLC_dx_Wb_per_m'),('dLC_dx_Wb_per_m','dLA_dx_Wb_per_m')]),
        'current_scenarios_not_ratings':[
            {'equivalent_phase_peak_A':i,'vector_A':math.sqrt(1.5)*i,'minimum_archived_force_N':kpkmin*i,'copper_loss20_W':1.5*rphase*i*i,'sinusoidal_phase_rms_current_density_A_mm2':i/math.sqrt(2)/area}
            for i in [0.1,0.5,0.75,1.,1.5,2.]]
    }
    return out

def force_svg(rows, old_rows):
    w,h=900,400
    xmin,xmax=-20,20
    ymin,ymax=2.30,2.56
    def xy(x,y): return 70+(x-xmin)/(xmax-xmin)*800, 330-(y-ymin)/(ymax-ymin)*270
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">', '<rect width="900" height="400" fill="white"/>','<g font-family="Arial,sans-serif" fill="#192d3e">','<text x="70" y="28" font-size="21">Archived optimum balanced-current force constant</text>','<text x="70" y="49" font-size="13">N/A of current-vector magnitude — simulation, not measured force</text>']
    for val in [2.30,2.35,2.40,2.45,2.50,2.55]:
        _,y=xy(0,val); parts += [f'<line x1="70" y1="{y}" x2="870" y2="{y}" stroke="#dbe4ec"/>',f'<text x="22" y="{y+4}" font-size="13">{val:.2f}</text>']
    for val in [-20,-10,0,10,20]:
        x,_=xy(val,2.3); parts.append(f'<text x="{x-10}" y="351" font-size="13">{val}</text>')
    for label,data,color in [('Rev62',old_rows,'#7a8190'),('Rev64',rows,'#007f8b')]:
        points=' '.join(f'{xy(r["relative_position_mm"],r["KF_unit_N"])[0]:.2f},{xy(r["relative_position_mm"],r["KF_unit_N"])[1]:.2f}' for r in data)
        parts.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="2.5"/>')
    parts.extend(['<text x="365" y="380" font-size="14">Position relative to centre (mm)</text>','<text x="720" y="75" fill="#7a8190" font-size="14">Rev62</text>','<text x="800" y="75" fill="#007f8b" font-size="14">Rev64</text>','</g></svg>'])
    return '\n'.join(parts)+'\n'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parameters',type=Path,default=ROOT/'calculations/parameters.json')
    ap.add_argument('--output',type=Path,default=ROOT/'calculations')
    args=ap.parse_args()
    p=json.loads(args.parameters.read_text(encoding='utf-8'))
    rows=load_rows(ROOT/'simulation/rev64/Rev64_CENTERED_COIL_PM_KF.csv')
    old=load_rows(ROOT/'archive/recovered-history/Rev62_CENTERED_COIL_PM_KF.csv')
    out=calculate(p,rows,old)
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/'results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    md=['# Generated calculation results','', 'Generated from explicit parameters and archived CSV data. Electrical estimates include the assumed 0.20 m extra wire per coil. Current examples are not operating ratings. Changing geometry does not resimulate the archived force constants.','', '| Quantity (units in name) | Value |','|---|---:|']
    md += [f'| {k.replace("_", " ")} | {v:.9g} |' for k,v in out.items() if isinstance(v,(int,float))]
    md += ['','## Current examples — not approved limits','','| Equivalent phase peak A | Vector A | Minimum archived force N | Copper loss at 20°C W | Phase RMS current density A/mm² |','|---:|---:|---:|---:|---:|']
    md += ['| '+' | '.join(f'{v:.5g}' for v in row.values())+' |' for row in out['current_scenarios_not_ratings']]
    md += ['', 'Resistance and loss rise with temperature. Force uses a first-pass magnetic model with no temperature derating.','','![Archived force comparison](force-comparison.svg)']
    (args.output/'results.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    (args.output/'force-comparison.svg').write_text(force_svg(rows,old),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['coil_resistance20_ohm','six_coils_plus_trial_purchase_m','Rev64_k_phase_peak_equivalent_mean_N_per_A','historical_horizontal_equivalent_peak_current_A','historical_vertical_equivalent_peak_current_A']},indent=2))

if __name__=='__main__': main()
