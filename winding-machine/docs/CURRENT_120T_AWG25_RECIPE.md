# Current 120-turn AWG25 winding recipe

This is the **only** active coil-winding instruction. The CAD and documents elsewhere in `winding-machine/` were built around the earlier Rev64 80-turn, 0.250 mm wire coil and are retained as winder hardware references only. Do not use their 80-turn layer schedules.

## Trial coil specification

| Item | Value |
|---|---:|
| Coil count for one rail | 9 |
| Former / winding bore | 13.0 mm |
| Axial winding width | 5.0 mm |
| Turns | 120 |
| Copper | AWG25, 0.455 mm bare / about 0.496 mm finished |
| Prepared wire | 7.5 m per coil |
| Coil64 estimate | 238 µH, 0.752 Ω at 20 C, 7.088 m excluding leads, 10.326 g copper, reported 14 layers |
| Target finished geometry | 5 mm width × about 26 mm OD — measure; do not assume it fits until trialled |

## Winder setup

1. Use a removable 13.0 mm mandrel with release agent compatible with EL160. Keep the wire guide aligned with the middle of the 5 mm winding zone.
2. Set the spindle to 30 rpm for the first coil. Maintain only enough tension to lay the wire tightly without damaging enamel.
3. Use the 2 mm-pitch threaded rod guide. With a 200-step motor at 16 microsteps, the starting value is 1,600 guide steps/mm.
4. **Do not use an automatic 80-turn or fixed layer recipe.** The effective packing pitch depends on the actual coated diameter, tension and former. The Coil64 14-layer estimate is a geometry estimate, not a proven traverse program.
5. Wind one 120-turn sample, photograph every layer, and record its final bore, OD, width, resistance at measured temperature and wire length. Then tune the guide rate from that coil before producing the other eight.
6. Impregnate with EL160 according to the supplier cure/post-cure schedule. Measure again after cure before finalising the carrier CAD.

Use [the winding trial record](../../records/winding-trial.md) for each sample.
