-- Rev64: 0.5 mm bobbin wall, 4 x 1.7 mm winding windows, 80 turns.
-- Source geometry is ALREADY centred. Do not apply the old -36 mm shift.
-- FEMM Lua 4.0. Change these two folders if moving this package.
BASE_DIR = "C:/Users/invis/Documents/Codex/2026-09-06/referenced-chatgpt-conversation-this-is-an/outputs/Rev64_FEMM/"
WORK_DIR = "C:/Users/invis/Documents/Codex/2026-09-06/referenced-chatgpt-conversation-this-is-an/work/femm64/"
STEP_MM = 0.25
HALF_SPAN_MM = 20
LABEL_X = 7.55
COIL_Y = {-20,-12,-4,4,12,20}

function move_pack(dz)
    mi_clearselected()
    mi_selectgroup(100)
    mi_movetranslate(0,dz,4)
    mi_clearselected()
end
function progress(s)
    pf=openfile(WORK_DIR .. "progress.txt","w")
    write(pf,s,"\n")
    closefile(pf)
end
function set_current(a,b,c)
    mi_modifycircprop("A",1,a)
    mi_modifycircprop("B",1,b)
    mi_modifycircprop("C",1,c)
end
function force(a,b,c,pos)
    set_current(a,b,c)
    mi_analyze(1)
    mi_loadsolution()
    mo_clearblock()
    for j=1,6 do mo_selectblock(LABEL_X,COIL_Y[j]+pos) end
    result=mo_blockintegral(12)
    mo_clearblock()
    mo_close()
    return result
end

progress("Starting Rev64")
open(BASE_DIR .. "Rev64_CENTERED_0p5mm_BOBBIN_80T.fem")
mi_saveas(WORK_DIR .. "Rev64_WORKING.fem")
set_current(0,0,0)
x={}; la={}; lb={}; lc={}; ia={}; ib={}; ic={}; kf={}
n=floor(2*HALF_SPAN_MM/STEP_MM+0.5)
move_pack(-HALF_SPAN_MM)
for k=0,n do
    pos=-HALF_SPAN_MM+k*STEP_MM
    mi_analyze(1)
    mi_loadsolution()
    a,v,aa=mo_getcircuitproperties("A")
    b,v,bb=mo_getcircuitproperties("B")
    c,v,cc=mo_getcircuitproperties("C")
    mo_close()
    idx=k+1; x[idx]=pos; la[idx]=aa; lb[idx]=bb; lc[idx]=cc
    progress(format("PM sweep %d/%d; position %.2f mm",k+1,n+1,pos))
    if k<n then move_pack(STEP_MM) end
end
move_pack(-HALF_SPAN_MM)
f=openfile(BASE_DIR .. "Rev64_CENTERED_COIL_PM_KF.csv","w")
write(f,"relative_position_mm,lambdaA_Wb,lambdaB_Wb,lambdaC_Wb,dLA_dx_Wb_per_m,dLB_dx_Wb_per_m,dLC_dx_Wb_per_m,KF_unit_N,IA_norm,IB_norm,IC_norm\n")
for k=1,n+1 do
    left=k-1; right=k+1
    if k==1 then left=1 end
    if k==n+1 then right=n+1 end
    dx=(x[right]-x[left])/1000
    ga=(la[right]-la[left])/dx
    gb=(lb[right]-lb[left])/dx
    gc=(lc[right]-lc[left])/dx
    avg=(ga+gb+gc)/3
    pa=ga-avg; pb=gb-avg; pc=gc-avg
    kf[k]=sqrt(pa*pa+pb*pb+pc*pc)
    ia[k]=pa/kf[k]; ib[k]=pb/kf[k]; ic[k]=pc/kf[k]
    write(f,format("%.6f,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g\n",x[k],la[k],lb[k],lc[k],ga,gb,gc,kf[k],ia[k],ib[k],ic[k]))
end
closefile(f)

-- Fresh vectors and predictions come from THIS sweep, not Rev62 constants.
f=openfile(BASE_DIR .. "Rev64_PM_ODD_DIRECT_FORCE_VALIDATION.csv","w")
write(f,"relative_position_mm,IA_unit_A,IB_unit_A,IC_unit_A,F_plus_N,F_minus_N,F_PM_odd_N,F_even_N,Rev64_KF_unit_N,difference_N,difference_percent\n")
test={1,floor(n/2)+1,n+1}
current_position=0
for j=1,3 do
    k=test[j]; pos=x[k]
    move_pack(pos-current_position); current_position=pos
    fp=force(ia[k],ib[k],ic[k],pos)
    fm=force(-ia[k],-ib[k],-ic[k],pos)
    odd=(fp-fm)/2; even=(fp+fm)/2; diff=odd-kf[k]
    write(f,format("%.6f,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g\n",pos,ia[k],ib[k],ic[k],fp,fm,odd,even,kf[k],diff,100*diff/kf[k]))
    progress(format("Direct force %d/3; position %.2f mm",j,pos))
end
closefile(f)
move_pack(-current_position)
set_current(0,0,0)
mi_saveas(WORK_DIR .. "Rev64_RESTORED_CENTERED.fem")
mi_close()
progress("COMPLETE: 161 PM positions and 6 direct-force solves")
quit()
