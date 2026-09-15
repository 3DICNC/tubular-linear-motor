# Bill of materials and procurement

> **Historical Rev64 reference — not the active build.** This file describes the recovered six-coil / 80-turn Rev64 concept. It does not define the current nine-coil prototype. Use [the current prototype definition](11-current-build.md), [one-rail BOM](12-one-rail-bom.md), and [project audit](13-project-audit.md) for active work.

This is a complete register of known parts and unresolved systems, not a fully orderable production BOM. Blank prices and supplier fields mean unknown, not zero. No total build cost can be stated until those items are selected. The machine-readable [BOM](../bom/bom.json) retains supplier, part-number and cost fields for future quotes.

| ID | Item | Quantity | Specification | Status |
|---|---|---:|---|---|
| MAG-01 | Axially magnetized disc magnet | 16 each | Ø10 × 5 mm; N42SH model label; coating and supplier properties pending | Geometry defined; material certificate needed |
| POL-01 | Steel pole ring | 7 each | Ø10 OD × Ø5 ID × 2 mm; steel grade/B-H curve pending | Geometry defined; alloy pending |
| TUB-01 | Carbon tube | 1 each | Ø12 OD × Ø10.2 ID × 94 mm; layup and tolerances pending | Nominal geometry defined |
| BOB-01 | Six-pocket bobbin | 1 each | Ø12.4 ID, Ø13.4 base OD, Ø16.8 lands, 45 mm length; material/process/routes pending | Provisional custom part |
| WND-01 | Wound coil | 6 each | 80 turns; 4 mm width; Ø13.4–16.8 mm envelope | Trial winding required |
| WIRE-01 | Enamelled copper wire | TBD m | 0.250 mm bare; Grade 1; ≤0.281 mm finished; see calculated procurement length | Trial purchase only; full-build quantity calculated |
| BOB-TRIAL | Single-pocket trial former | 1 each | Rev64 pocket dimensions; actual lead/crossover design required | Additional prototype tooling; CAD not supplied |
| ADH-01 | Adhesive / impregnation | TBD quantity TBD | Compatibility, cure and thickness to be selected | Open |
| RET-01 | Stack retention and assembly fixture | TBD set TBD | End retention, magnet forces and tolerances to be designed | Open |
| GUIDE-01 | Linear guidance and carriage | TBD set TBD | Travel/load/stiffness, attachment and alignment to be specified | Open |
| STOP-01 | Mechanical stops and limit system | TBD set TBD | Usable stroke and failure behaviour to be specified | Open |
| LEAD-01 | Lead harness and terminals | TBD set TBD | Flexible leads, strain relief, connectors and phase topology to be detailed | Open |
| ENC-01 | Position sensor and mount | TBD set TBD | Accuracy, resolution, interface and datum pending | Open |
| DRV-01 | Three-phase current controller | 1 set | Current convention, inductance, bus voltage and encoder compatibility pending | Selection open; no rated current established |
| PSU-01 | Power supply and electrical protection | 1 set | Bus voltage/current, energy handling and protection pending | Selection open |
| TEMP-01 | Temperature sensors | TBD quantity TBD | Sensor placement, range and electrical isolation pending | Open |
| TEST-01 | Test equipment | 1 set | Suitable micrometer, resistance instrument, calibrated load cell, current measurement and temperature logging | Equipment checklist; not motor mass |

WND-01 is the wound subassembly and WIRE-01 is its raw material: do not count both as purchased finished coils plus purchased winding wire unless intentionally outsourcing spares. The trial former is additional tooling, not part of the 31-solid assembly. The reference annulus is excluded from the BOM.

Use the generated calculations for wire consumption and the separate full-build-plus-trial purchase allowance. Obtain a small trial spool before a production order. Confirm magnet coating dimensions, actual tube tolerances and bobbin process before releasing custom parts.

