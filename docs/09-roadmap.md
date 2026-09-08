# Open decisions and milestones

| ID | Decision / work | Required evidence | Status |
|---|---|---|---|
| M1 | Confirm axis orientation, moving mass, acceleration and stroke | Updated requirements including gravity, friction and cable forces | Open |
| M2 | Qualify wire and single-pocket winding | Supplier certificate and measured 80-turn sample after cure | Open |
| M3 | Detail bobbin and crossover channels | Material/process choice, tolerance drawing and lead routing | Open |
| M4 | Detail magnet retention and tube installation | Adhesive gaps, fixture, end retention and tolerance stack | Open |
| M5 | Design guidance, carriage, stops and sensor mount | Assembly CAD, loads, stiffness and measured free travel | Open |
| M6 | Confirm electrical topology and polarity | Terminal drawing, individual coil/phase resistance and polarity record | Open |
| M7 | Improve and validate electromagnetics | Material curves, mesh/boundary study and calibrated force measurements | Open |
| M8 | Select driver, encoder and power supply | Inductance/back-EMF data, required speed, current convention and interface | Open |
| M9 | Establish thermal and duty limits | Stable tests in final mounting and worst ambient | Open |
| M10 | Release prototype build | Closed deviations, complete BOM and approved manufacturing drawings | Open |

Recommended order: requirements confirmation and wire procurement in parallel, then the single-pocket trial, mechanical detailing, full coil assembly, restrained electrical/force tests, and thermal qualification. Changing wire gauge, turn count, coil geometry or adding magnetic hardware requires re-evaluating force and electrical calculations.

## Change control

Keep recovered CAD and simulation files unchanged as baselines. Put design changes under a new revision directory. Describe changed dimensions, reason, source evidence and affected calculations. Generate fresh STEP exports, rerun relevant simulations and compare against baseline. Attach build/test evidence to the same revision. Do not promote an assumption to a measured fact without a record.

The GitHub issue template supports each milestone's requirements, evidence and acceptance criteria. This repository is the requested GitHub project; a separate GitHub Projects board is not assumed.
