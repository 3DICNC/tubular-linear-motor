# Rev64 FEMM — 0.50 mm bobbin wall

`Rev64_CENTERED_0p5mm_BOBBIN_80T.fem` is the updated centred model. The complete six-coil geometry remains group 100, with winding radius 6.7 to 8.4 mm, four-millimetre width, centres -20, -12, -4, 4, 12 and 20 mm, phase order A-B-C-A-B-C and 80 turns per coil. Stationary nodes, segments and labels are unchanged from Rev62. The nonmagnetic bobbin is represented by the default air material, as in Rev62.

`Rev64_sweep_and_validate.lua` runs the 161-position PM flux-linkage sweep and then performs positive/negative direct-force checks at -20, 0 and +20 mm. It starts from an already-centred FEM file, so it does not apply the old -36 mm centring translation.

The average Rev64 unit-vector force constant is 2.375722 N/A, ranging from 2.351048 to 2.412174 N/A. Rev62 averaged 2.485202 N/A, so moving the windings outward for the thicker bobbin reduces the average by 4.405%. For sinusoidal phase peak scaling, multiply by sqrt(3/2): the Rev64 range is approximately 2.879 to 2.954 N/A phase peak, averaging 2.910 N/A phase peak.

The direct PM-odd force results agree with the derivative prediction within 0.35% at the three validation positions. The largest even-force residual is 0.000059 N. These values describe the existing first-pass static FEMM material model and do not include temperature, magnetic saturation curves, PWM or carbon-tube eddy-current effects.
