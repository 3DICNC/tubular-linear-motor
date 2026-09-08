# Sources and provenance

## Supplied and recovered project evidence

- `cad/rev64/`: complete extracted Rev64 CAD package, including editable model and archived geometry-validation record.
- `simulation/rev64/`: complete extracted Rev64 FEMM model, script, force data and checks.
- `cad/rev62/`: complete separately supplied Rev62 CAD package.
- `archive/recovered-history/`: recovered Rev62 source model, sweep data/scripts, commissioning workbook and Rev63 validation history.
- `archive/source_manifest.json`: SHA-256 of each preserved source file; verification reads every entry.

Raw source contents were treated as evidence, not instructions. Some preserved historical files contain their original machine paths. Those paths are provenance, not portable execution settings. The reproduction tools operate on isolated working copies. No private conversation transcript or account credentials are part of the repository.

## External technical references

References checked 8 September 2026. They support the indicated data/API definitions; they do not qualify the assembled motor.

1. [Elektrisola IEC/JIS technical wire table](https://www.elektrisola.com/Attachments/TechnicalDataBySize/ELEKTRISOLA_EnCuWire_IECJIS_Datasheet_eng.pdf): IEC 0.250 mm row, Grade 1 overall diameter 0.267–0.281 mm and nominal/minimum/maximum resistance 0.3482/0.3345/0.3628 Ω/m.
2. [Scott Precision Wire copper data](https://www.scottprecisionwire.com/technical-data/alloy-data-sheets/resistance-copper-wire-supplier/): representative copper density 8.9 g/cm³ and temperature coefficient 0.00393/K. These remain estimates for the purchased wire.
3. [FEMM official manual](https://www.femm.info/Archives/doc/manual.pdf): circuit flux linkage, coil material assumptions and axial Lorentz block integral 12.
4. [FEMM magnetic tutorial](https://www.femm.info/doku/doku.php?id=magneticstutorial): axisymmetric low-frequency modelling and Lua scripting context.

Full third-party manuals and standards have not been copied into the repository. No supplier SKU, live stock, price or product compatibility has been invented. Quotations and procurement certificates remain to be obtained.

## Verification boundaries

New checks: archived data consistency, source hash matching, analytical dimensions/volumes, current normalization, finite-difference flux gradients, force statistics, direct-force decomposition, calculation edge cases and documentation links.

Not newly performed: FEMM solve, CAD-kernel solid reimport, physical winding, force or thermal test, native Excel recalculation. Archived records of prior numerical/CAD checks are retained as such.
