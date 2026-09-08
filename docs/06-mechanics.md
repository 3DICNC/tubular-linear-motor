# Mechanical assembly and tolerances

## Nominal geometry is not a shop drawing

The CAD includes five full-width 4 mm separator lands and two 0.5 mm end flanges. These were provisional additions in Rev62 and remain provisional in Rev64. Bobbin material candidates PEEK or G10 appear in the old workbook; neither is a selected, qualified process for this geometry.

Define manufacturing tolerances on the actual drawing before ordering final custom parts. In particular, Ø12.4 bore and Ø12 tube give only 0.20 mm nominal radial clearance. Tube straightness, ovality, bobbin shrinkage, guidance alignment and temperature expansion all contribute to minimum running clearance.

For measured worst-case diameters, radial clearance c_min = (bobbin_ID_min − tube_OD_max)/2 − eccentricity_allowance. Similar stack-to-tube clearance is (tube_ID_min − magnet_OD_max)/2 before coating and assembly allowances. A numerical tolerance budget requires those actual limits.

The nominal winding OD allowance relative to the reference bore is only (17 − 16.8)/2 = 0.10 mm, but no physical reference housing is selected. Do not use this as a verified bearing fit.

## Assembly sequence to develop

1. Inspect magnet dimensions, axial magnetization and pole-ring geometry. Confirm pole material and magnet supplier certificate. Use a suitable fixture for the interacting magnets; the alternating stack contains repelling interfaces and needs defined retention.
2. Define adhesive gaps and end retention, then calculate the assembled stack length and revise CAD/FEMM if the nominal 94 mm changes.
3. Trial the fixed stack inside the measured carbon tube without damaging coatings. Do not treat the Ø5 pole-ring holes as a continuous bore through the solid magnets.
4. Complete the single-pocket winding trial and winding inspection before committing to the six-pocket former.
5. Add coil crossover routes, lead exits and strain relief while preserving the required radial envelope. Record any geometry change as a new revision.
6. Design carriage attachment, guides, end stops and encoder datum together. The winding pack must not carry unspecified lateral loads through rubbing contact with the tube.
7. Confirm free travel and measured margins with the assembled lead harness before electrical commissioning.

This is a development sequence. Detailed retention, guidance and connection drawings remain required for assembly release.

## Material and environment requirements

Record bobbin modulus, creep behaviour and temperature limit; adhesive cure shrinkage and temperature range; tube thermal expansion, straightness and conductivity; magnet temperature-dependent properties and coating. The minimum compatible limit of the insulation/material system constrains operation. Carbon composite properties depend on layup, so a generic isotropic assumption does not establish thermal or mechanical performance.

Mass, stiffness, buckling, bearing life and fatigue calculations are pending the carriage, support spans, material properties, load directions and duty cycle. Do not substitute the 0.5 kg historical carriage target for a measured moving assembly mass.
