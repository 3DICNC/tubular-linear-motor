# Revision history and workbook audit

## Revision 62 to Revision 64

| Parameter | Rev62 | Rev64 |
|---|---:|---:|
| Bobbin bore, mm | 12.4 | 12.4 |
| Bobbin base wall, mm | 0.10 | 0.50 |
| Winding inside diameter, mm | 12.6 | 13.4 |
| Winding outside diameter, mm | 16.8 | 16.8 |
| Radial winding window, mm | 2.1 | 1.7 |
| Axial winding window, mm | 4 | 4 |
| Window area, mm² | 8.4 | 6.8 |
| Turns per coil | 80 | 80 |
| Coil pitch, mm | 8 | 8 |

The wall is five times as thick; available winding-window cross-section decreases by 19.0476%. Increased wall thickness is not itself proof of adequate strength. The magnet stack, carbon tube, coil axial positions and nominal travel are unchanged. The archived mean force constant falls from 2.485202 to 2.375722 N/A of current-vector magnitude, a 4.4053% decrease.

Revision 62 CAD is already centred, but its original parent FEMM coil centres were 16, 24, 32, 40, 48, 56 mm. Its sweep translated the pack by −36 mm. Revision 64 FEMM is already centred; repeating that translation is incorrect.

## What the recovered workbook establishes

The preserved `archive/recovered-history/Rev62_build_and_commissioning_log.xlsx` was inspected across all five worksheets. It is a commissioning template, not evidence of a completed build.

| Sheet / cells | Findings and implications |
|---|---|
| Baseline B9:B15 | 0.10 mm wall, 6.3 mm copper start radius, 2.1 mm radial window and generic AWG30 candidate are Rev62 values. They must not be applied to Rev64. |
| Baseline B19:B21 | Historical target mass 0.5 kg and acceleration 5.186 m/s² imply 2.593 N inertia-only thrust. Orientation, friction and total moving mass need confirmation. |
| Baseline B22:B25 | 0.75, 1.5, 2.0 and 2.5 A phase-peak entries are proposed test/candidate values, not approved ratings. |
| Build QC D7:D12; E17:K23 | Actual dimensions, winding counts, resistances and insulation results are empty. Status entries are Pending. |
| Build QC C18:C23 | Coil positions use the old uncentred FEMM frame (16 to 56 mm). New records use centred coordinates. |
| Thermal Log B34:B36 | 2.63 Ω is an estimated phase resistance, 120°C is an old proposed copper limit, and <1°C rise over 10 minutes is an old steady-state criterion. None proves safe operation. |
| Thermal Log rows 6:30 | Raw test inputs are blank. Formulas are present, but no measured thermal run is recorded. |
| Force Travel rows 6:8 | Measured F+ and F− are blank. Force targets and current vectors belong to the earlier revision. |
| Release rows 6:15 | Every disposition is Pending; no release evidence is filled. |

The old thermal temperature estimate divides by an estimated reference resistance. For new tests, measure the same winding's resistance and reference temperature first. The old force target cells are constants and do not automatically scale if the current input changes. New record guidance requires recalculating each target for the actual current and position.

## Recovery provenance

The recovered Rev62 parent FEMM file exactly matches the SHA-256 parent fingerprint recorded in Rev64's source check. The Rev62 CAD README in the later supplied archive is identical to the earlier recovered note. Raw source files are preserved without revision substitutions. Revision 63 direct-force files are retained as history and are not used as Rev64 results.
