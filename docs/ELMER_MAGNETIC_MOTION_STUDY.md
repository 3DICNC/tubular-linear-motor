# Elmer magnetic motion study — withdrawn

The uploaded animation is **not a valid moving-coil electromagnetic result** and must not be used for force, field uniformity, or motor-performance decisions.

It was produced from three coarse magnetostatic meshes. The permanent-magnet field was solved, but the moving coil was not represented with the correct 120-turn, three-phase current distribution or commutation at each position. The visual therefore looks incorrect because it mainly shows the fixed magnet field.

## Replacement work required

A valid study will use:

- the fixed 10 × 10 mm magnet and 10 × 2 mm steel-button stack;
- the actual 9-coil A–B–C layout;
- the correct current density for 120 turns at the commanded phase current;
- phase-current changes at each position; and
- a consistent refined mesh and force extraction.

The local Elmer files are retained as a solver-setup experiment only.