# Rev62 nominal CAD assembly

Open `Rev62_centered_assembly.step` in your CAD application. It contains 31 named solid components, in millimetres, with the motor axis along Z and the coil pack centred at Z=0. The STEP solids retain analytic cylindrical geometry; these are actual solid CAD files.

`Rev62_parametric_model.scad` is the editable OpenSCAD model. Change the parameters at its top or in the Customizer. Set `cutaway=true` for an axial half-section, select a component with `part`, or change `position` between -20 and +20 mm to move the complete winding pack and bobbin. Changes to dimensions require new electromagnetic and mechanical checks. The supplied STEP files are the nominal configuration and do not update automatically when the SCAD model is edited.

## Included components

| Component | Quantity | Nominal dimensions, mm |
|---|---:|---|
| Magnet discs | 16 | OD 10, axial length 5; paired into eight 10 mm sections |
| Steel pole rings | 7 | OD 10, ID 5, axial length 2 |
| Carbon tube | 1 | OD 12, ID 10.2, axial length 94 |
| Winding envelopes | 6 | OD 16.8, ID 12.6, axial length 4; 8 mm pitch |
| Provisional bobbin | 1 | ID 12.4, base OD 12.6, land/flange OD 16.8, overall length 45 |

Coils C1–C6 are ordered in increasing Z, at -20, -12, -4, 4, 12 and 20 mm; phases A–B–C–A–B–C, 80 turns each. Copper solids represent winding envelopes, not individual wires or solid-copper manufactured rings.

The magnetic stack and tube extend from Z=-47 to +47. Magnet pair centres are -42, -30, -18, -6, 6, 18, 30 and 42. The first pair is magnetized +Z, followed by alternating -Z/+Z pairs. Both 5 mm discs within one pair share the same magnetization. Pairing 10 mm FEMM sections into two physical 5 mm discs follows the earlier build specification; there is no adhesive thickness or gap between them in this nominal model.

## Source and interpretation

Geometry was checked against `E:/temp/Rev62_4mm_COILS_2.1mm_RADIAL_80T_ROBUST_BOBBIN.fem`. The source file still has coil centres 16 to 56 mm; the supplied CAD applies the sweep's -36 mm centring translation to the coils only. Its 24 coil nodes, 24 segments and six labels belong to group 100. Magnet labels are group 10; steel labels are group 20; the tube label is group 30. Physical bobbin geometry was not explicitly drawn in FEMM.

The pole regions have a boundary at radius 2.5 mm and a steel label outside that boundary. Their inner regions have no steel label and use the default air material: the matching CAD parts are rings, not full discs.

The FEMM annulus at radius 8.5–11.5 mm has no assigned block label. It therefore does not establish a physical steel yoke. Its separate `REFERENCE_ONLY.step` file preserves that geometry for inspection and is excluded from the physical assembly. The air domain is also excluded. Adding a steel housing here would change the electromagnetic model.

## Provisional mechanical details

The previous selected bobbin ID and 0.10 mm wall were retained. To make a complete solid former with six 4 mm winding pockets, this CAD adds five full-width 4 mm intercoil lands and two 0.5 mm end flanges. These dimensions are proposed here, not recovered from FEMM. The former uses nonmagnetic material in space treated as air by FEMM; final material selection, tolerances and fabrication method remain open. The thin wall is a nominal design value, not a demonstrated manufacturing capability.

Leads, winding crossover channels, insulation build, adhesive thickness, end retainers, bearings, carriage interfaces and external mounts are not yet defined. They require a subsequent mechanical detail revision before fabrication. No unspecified steel housing or central through-rod has been added.

## Verification

All nine STEP exports were reopened using the CAD kernel and checked for valid solid topology, expected solid counts and matching volumes. The main assembly contains 31 solids and has no positive-volume component intersections at the centred position. The analytical travel checks cover the entire continuous -20 to +20 mm interval because each coaxial moving component has a constant radial envelope. Minimum nominal radial gaps are 0.10 mm from magnets to tube and 0.20 mm from tube to bobbin. Coil OD is 0.10 mm radially inside the separate reference bore, if that bore is later used mechanically.

At both travel extremes, every coil remains inside the 94 mm magnetic stack, with a minimum axial margin of 5 mm. The 45 mm bobbin retains a minimum margin of 4.5 mm. These are geometry checks, not a bearing design or a tolerance analysis. `Rev62_geometry_validation.json` records dimensions, source fingerprint, component volumes, STEP reimport results and end-position checks. The PNG preview is a section rendering of the actual CAD solids.

Subassembly STEP files retain assembly coordinates. Reusable single magnet, pole ring and coil-envelope files have their lower face at Z=0. The isolated bobbin is centred at Z=0.
