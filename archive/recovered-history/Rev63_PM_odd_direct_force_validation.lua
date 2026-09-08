-- Rev63: direct PM-force validation of the final Rev62 robust-bobbin model.
-- Run Rev62_build_robust_bobbin_geometry.lua and Rev62_centered_coil_PM_KF_sweep.lua first.
-- FEMM Lua 4.0 compatible.

INPUT_FILE   = "E:\\temp\\Rev62_4mm_COILS_2.1mm_RADIAL_80T_ROBUST_BOBBIN.fem"
OUTPUT_CSV   = "E:\\temp\\Rev63_PM_ODD_DIRECT_FORCE_VALIDATION.csv"
RESTORED_FEM = "E:\\temp\\Rev63_RESTORED.fem"

CENTER_SHIFT_MM = -36.0
LABEL_X = 7.35

-- Exact Rev62 PM/KF CSV values at -20, 0, and +20 mm.
-- Each vector is balanced and unit Euclidean norm.
TEST_POS = { -20.0, 0.0, 20.0 }
TEST_IA  = { -0.438708467231, 0.409511296592, 0.815633332544 }
TEST_IB  = { -0.37701072225, -0.816495277119,-0.37530974189  }
TEST_IC  = {  0.815719189481, 0.406983980527,-0.440323590654 }
TEST_KF  = {  2.52593826279,  2.49104972207,  2.52341068009  }

COIL_Y = { -20.0, -12.0, -4.0, 4.0, 12.0, 20.0 }

function select_complete_coil_pack()
    mi_clearselected()
    mi_selectgroup(100)
end

function select_six_coils_in_solution(position_mm)
    mo_clearblock()
    for j = 1, 6 do
        mo_selectblock(LABEL_X, COIL_Y[j] + position_mm)
    end
end

function direct_lorentz_force(ia, ib, ic, position_mm)
    mi_modifycircprop("A", 1, ia)
    mi_modifycircprop("B", 1, ib)
    mi_modifycircprop("C", 1, ic)
    mi_analyze(1)
    mi_loadsolution()
    select_six_coils_in_solution(position_mm)
    fz = mo_blockintegral(12)
    mo_clearblock()
    mo_close()
    return fz
end

open(INPUT_FILE)
mi_saveas("E:\\temp\\Rev63_WORKING.fem")

-- Original coil pack [14,58] -> centred pack [-22,+22] mm.
select_complete_coil_pack()
mi_movetranslate(0, CENTER_SHIFT_MM, 4)
mi_clearselected()

f, err = openfile(OUTPUT_CSV, "w")
if f == nil then
    messagebox("Cannot open output CSV:\n" .. OUTPUT_CSV)
    return
end

write(f, "relative_position_mm,IA_unit_A,IB_unit_A,IC_unit_A,F_plus_N,F_minus_N,F_PM_odd_N,F_even_N,Rev62_KF_unit_N,difference_N,difference_percent\n")

current_position = 0.0
for k = 1, 3 do
    target_position = TEST_POS[k]
    delta = target_position - current_position
    if delta ~= 0 then
        select_complete_coil_pack()
        mi_movetranslate(0, delta, 4)
        mi_clearselected()
        current_position = target_position
    end

    fplus = direct_lorentz_force(TEST_IA[k], TEST_IB[k], TEST_IC[k], target_position)
    fminus = direct_lorentz_force(-TEST_IA[k], -TEST_IB[k], -TEST_IC[k], target_position)
    fpm_odd = (fplus - fminus) / 2.0
    feven = (fplus + fminus) / 2.0
    difference = fpm_odd - TEST_KF[k]
    difference_percent = 100.0 * difference / TEST_KF[k]

    write(f, format("%.6f,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g\n",
        target_position, TEST_IA[k], TEST_IB[k], TEST_IC[k], fplus, fminus,
        fpm_odd, feven, TEST_KF[k], difference, difference_percent))
end
closefile(f)

-- Restore the original Rev62 coil position and nominal circuit currents.
select_complete_coil_pack()
mi_movetranslate(0, -current_position - CENTER_SHIFT_MM, 4)
mi_clearselected()
mi_modifycircprop("A", 1, -1.0)
mi_modifycircprop("B", 1, 0.5)
mi_modifycircprop("C", 1, 0.5)
mi_saveas(RESTORED_FEM)

messagebox("Rev63 direct PM-force validation complete.\n\nUpload:\n" .. OUTPUT_CSV)
