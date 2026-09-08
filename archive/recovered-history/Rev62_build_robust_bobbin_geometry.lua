-- Rev62: buildable-bobbin geometry revision for Rev54.
-- FEMM Lua 4.0 compatible.
--
-- Physical radial stack selected for Option 2:
--   carbon tube OD:      12.00 mm  (r = 6.00 mm)
--   PEEK/G10 bobbin ID:  12.40 mm  (r = 6.20 mm)
--   bobbin wall:          0.10 mm
--   copper winding:       r = 6.30 .. 8.40 mm
--
-- This keeps the existing 16.80 mm wound OD and its 0.10 mm outer
-- clearance.  It intentionally reduces the copper radial window from
-- 2.20 to 2.10 mm.  Do not use AWG29 unless the measured finished wire
-- diameter proves the 80-turn pack fits; AWG30 is the conservative choice.
--
-- Axial coil topology and all magnet/steel geometry remain unchanged.

INPUT_FILE  = "E:\\temp\\Rev54_4mm_COILS_2.2mm_RADIAL_80T_CLEAN_REV5.fem"
OUTPUT_FILE = "E:\\temp\\Rev62_4mm_COILS_2.1mm_RADIAL_80T_ROBUST_BOBBIN.fem"

COIL_R_IN  = 6.30
COIL_R_OUT = 8.40
COIL_R_LABEL = (COIL_R_IN + COIL_R_OUT) / 2.0
COIL_CENTRES = { 16.0, 24.0, 32.0, 40.0, 48.0, 56.0 }
COIL_CIRCUITS = { "A", "B", "C", "A", "B", "C" }

open(INPUT_FILE)
mi_saveas(OUTPUT_FILE)

-- Group 100 is complete coil geometry only: 24 nodes, 24 segments,
-- and six copper labels.  Removing it cannot alter magnet/steel geometry.
mi_clearselected()
mi_selectgroup(100)
mi_deleteselected()
mi_clearselected()

for k = 1, 6 do
    zc = COIL_CENTRES[k]
    z0 = zc - 2.0
    z1 = zc + 2.0

    -- Recreate one 4.0 mm x 2.10 mm copper rectangle.
    mi_drawrectangle(COIL_R_IN, z0, COIL_R_OUT, z1)

    -- Assign its four nodes to the complete movable coil group.
    mi_clearselected()
    mi_selectnode(COIL_R_IN, z0)
    mi_selectnode(COIL_R_OUT, z0)
    mi_selectnode(COIL_R_OUT, z1)
    mi_selectnode(COIL_R_IN, z1)
    mi_setnodeprop("", 100)

    -- Assign its four segments to the same group.
    mi_clearselected()
    mi_selectsegment((COIL_R_IN + COIL_R_OUT) / 2.0, z0)
    mi_selectsegment(COIL_R_OUT, zc)
    mi_selectsegment((COIL_R_IN + COIL_R_OUT) / 2.0, z1)
    mi_selectsegment(COIL_R_IN, zc)
    mi_setsegmentprop("", 0, 1, 0, 100)

    -- Restore Copper material, the original phase order, 80 turns, and group.
    mi_addblocklabel(COIL_R_LABEL, zc)
    mi_selectlabel(COIL_R_LABEL, zc)
    mi_setblockprop("Copper", 1, 0, COIL_CIRCUITS[k], 0, 100, 80)
    mi_clearselected()
end

mi_saveas(OUTPUT_FILE)
messagebox("Rev62 geometry complete.\n\nCopper: r = 6.30 .. 8.40 mm\n" ..
    "Bobbin: ID 12.40 mm, wall 0.10 mm\n" ..
    "Magnets and steel: unchanged\n\nSaved:\n" .. OUTPUT_FILE)
