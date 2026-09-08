# Rev64 CAD — 0.50 mm bobbin wall

The assembly is centred at Z=0 and uses millimetres. Open `Rev64_centered_assembly.step` for the complete 31-solid assembly. The magnet/steel stack, carbon tube and axial coil positions are unchanged from Rev62. The bobbin base OD is now 13.4 mm (12.4 mm ID plus two 0.5 mm walls), so each winding envelope is ID 13.4 mm, OD 16.8 mm and 4 mm wide.

`Rev64_parametric_model.scad` is editable and has a `position` control from -20 to +20 mm. All STEP exports were reopened and passed solid-validity, solid-count and volume checks. There are no positive-volume component intersections. At both travel limits the coil windings retain 5 mm axial margin within the 94 mm magnet stack; the 45 mm provisional bobbin retains 4.5 mm.

The five 4 mm separator lands and two 0.5 mm end flanges remain proposed mechanical features. Lead exits, crossover channels, adhesive allowance, mounting and manufacturing tolerances still require detailing.

The usable winding window is 4.0 mm axial by 1.7 mm radial. The proposed 80-turn trial winding uses six layers: 14 + 14 + 13 + 13 + 13 + 13. Specify 0.250 mm bare copper with Grade 1 enamel and a guaranteed finished diameter no greater than 0.281 mm. That published maximum gives 1.686 mm radial build and 3.934 mm maximum axial occupation in an ideal ordered winding. It leaves only 0.014 mm radial and 0.066 mm axial nominal allowance, so the actual wire certificate and a trial winding are required. AWG30 heavy-build wire does not fit this window, and generic “AWG30” is not a sufficient purchase specification.

The copper parts are homogenized winding envelopes rather than individual wires. The separate unassigned outer-envelope STEP preserves FEMM reference geometry and is excluded from the physical assembly.
