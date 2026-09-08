-- Rev62: PM flux-linkage/KF sensitivity sweep for the robust-bobbin geometry.
-- Run Rev62_build_robust_bobbin_geometry.lua first.
-- FEMM Lua 4.0 compatible.

INPUT_FILE   = "E:\\temp\\Rev62_4mm_COILS_2.1mm_RADIAL_80T_ROBUST_BOBBIN.fem"
OUTPUT_CSV   = "E:\\temp\\Rev62_CENTERED_COIL_PM_KF.csv"
RESTORED_FEM = "E:\\temp\\Rev62_RESTORED.fem"

STEP_MM = 0.25
HALF_SPAN_MM = 20.0
CENTER_SHIFT_MM = -36.0

function select_complete_coil_pack()
    mi_clearselected()
    mi_selectgroup(100)
end

open(INPUT_FILE)
mi_saveas("E:\\temp\\Rev62_WORKING.fem")

select_complete_coil_pack()
mi_movetranslate(0, CENTER_SHIFT_MM, 4)
mi_clearselected()

f, err = openfile(OUTPUT_CSV, "w")
if f == nil then
    messagebox("Cannot open output CSV:\n" .. OUTPUT_CSV)
    return
end

write(f, "relative_position_mm,lambdaA_Wb,lambdaB_Wb,lambdaC_Wb,dLA_dx_Wb_per_m,dLB_dx_Wb_per_m,dLC_dx_Wb_per_m,KF_unit_N,IA_norm,IB_norm,IC_norm\n")

n = floor((2.0 * HALF_SPAN_MM) / STEP_MM + 0.5)
x = {}
la = {}
lb = {}
lc = {}

select_complete_coil_pack()
mi_movetranslate(0, -HALF_SPAN_MM, 4)
mi_clearselected()

for k = 0, n do
    pos = -HALF_SPAN_MM + k * STEP_MM

    mi_modifycircprop("A", 1, 0)
    mi_modifycircprop("B", 1, 0)
    mi_modifycircprop("C", 1, 0)
    mi_analyze(1)
    mi_loadsolution()

    IA0, VA0, LA0 = mo_getcircuitproperties("A")
    IB0, VB0, LB0 = mo_getcircuitproperties("B")
    IC0, VC0, LC0 = mo_getcircuitproperties("C")
    mo_close()

    idx = k + 1
    x[idx] = pos
    la[idx] = LA0
    lb[idx] = LB0
    lc[idx] = LC0

    if k < n then
        select_complete_coil_pack()
        mi_movetranslate(0, STEP_MM, 4)
        mi_clearselected()
    end
end

select_complete_coil_pack()
mi_movetranslate(0, -HALF_SPAN_MM, 4)
mi_clearselected()

for k = 1, n + 1 do
    if k == 1 then
        dx = (x[2] - x[1]) / 1000.0
        ga = (la[2] - la[1]) / dx
        gb = (lb[2] - lb[1]) / dx
        gc = (lc[2] - lc[1]) / dx
    elseif k == n + 1 then
        dx = (x[k] - x[k-1]) / 1000.0
        ga = (la[k] - la[k-1]) / dx
        gb = (lb[k] - lb[k-1]) / dx
        gc = (lc[k] - lc[k-1]) / dx
    else
        dx = (x[k+1] - x[k-1]) / 1000.0
        ga = (la[k+1] - la[k-1]) / dx
        gb = (lb[k+1] - lb[k-1]) / dx
        gc = (lc[k+1] - lc[k-1]) / dx
    end

    gmean = (ga + gb + gc) / 3.0
    pa = ga - gmean
    pb = gb - gmean
    pc = gc - gmean
    normp = sqrt(pa*pa + pb*pb + pc*pc)

    if normp > 0 then
        ia = pa / normp
        ib = pb / normp
        ic = pc / normp
        kf = normp
    else
        ia = 0
        ib = 0
        ic = 0
        kf = 0
    end

    write(f, format("%.6f,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g\n",
        x[k], la[k], lb[k], lc[k], ga, gb, gc, kf, ia, ib, ic))
end

closefile(f)

select_complete_coil_pack()
mi_movetranslate(0, -CENTER_SHIFT_MM, 4)
mi_clearselected()
mi_modifycircprop("A", 1, -1.0)
mi_modifycircprop("B", 1, 0.5)
mi_modifycircprop("C", 1, 0.5)
mi_saveas(RESTORED_FEM)

messagebox("Rev62 PM/KF sweep complete.\n\nUpload:\n" .. OUTPUT_CSV)
