# Commissioning and measurement records

The recovered workbook contains no completed test evidence. Use the empty [Rev64 record templates](../records/README.md) for new measurements. Every measurement needs a build identifier, revision, date, instrument and calibration/reference information. Preserve raw readings separately from calculations.

## Stage 1: winding and mechanical fit

Record actual wire diameter, bobbin dimensions, layer count, turn count, final OD/width, lead length, resistance and measurement temperature. Inspect insulation and strain relief. Confirm the intended cure does not cause interference. Release the six-coil build only after the single-pocket trial passes a defined drawing and electrical inspection.

## Stage 2: phase and encoder verification

Confirm each series pair's polarity. Measure all coil resistances individually before joining, then each phase and line-to-line resistance under the selected topology. Record reference temperatures. Verify the encoder datum at magnetic centre and restrained motion direction. Initial ±18 mm soft limits are historical proposals; establish mechanical stops and verify usable travel before adopting them.

## Stage 3: static force

Use a restrained fixture and calibrated load cell. Record actual IA, IB, IC, position, F+ and F−, including force sign and zero offset. Obtain the current vector for the actual position from Rev64 data and state the scale. Compute F_pred = g·i, F_odd = (F+ − F−)/2 and F_even = (F+ + F−)/2. Use the same coordinate and force sign conventions throughout.

The saved file's IA_norm/IB_norm/IC_norm entries have unit vector magnitude, not unit phase peak. For equivalent phase-peak scale Ipk, multiply them by sqrt(3/2)Ipk. Recalculate the predicted target if current changes. Do not copy the old workbook's fixed Rev62 target numbers into a new run.

## Stage 4: thermal characterization

Select compatible material temperature limits and an initial restrained, current-limited test plan before applying power. The old workbook's current candidates and 120°C entry are not approved Rev64 settings. Record waveform, all relevant currents, ambient, elapsed time, duty, coil sensor temperatures, phase resistance, reference resistance/temperature, assembly state and stop reason.

Calculate copper loss from actual phase currents and temperature-corrected resistances. For unequal phase resistances, sum R_A i_A² + R_B i_B² + R_C i_C². Resistance thermometry estimates average winding temperature. A surface NTC and a resistance estimate can miss a local hot spot, so record both where available.

The old <1°C over 10 minutes criterion may be a useful proposed stability check, but dwell time and acceptable drift must be specified for the finished assembly. Establish thermal resistance only from stable readings with known mounting and ambient conditions. Current promotion needs measured evidence, not extrapolation from a short cold pulse.

## Release evidence

Before declaring continuous or peak ratings, close winding fit, all coil inspections, polarity, guidance, retention, limits, force mapping, thermal characterization and controller protection. Peak current needs an explicit duration, repetition/duty, starting temperature and cooling condition. Continuous force needs a defined ambient and mounting arrangement. Record unresolved deviations and do not label a pending item as passed.
