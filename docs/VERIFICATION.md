# Documentation verification

Completed on 8 September 2026 using the bundled Python runtime.

- All 43 preserved source files matched their source manifest hashes.
- The Rev62 parent and Rev64 derived FEMM files matched the fingerprints recorded in the source check.
- All 161 Rev64 data positions, finite-difference flux gradients, balanced current vectors and force constants were checked.
- All three archived direct-force decompositions and reported differences were checked.
- Analytical volumes matched all 31 CAD component records; nominal end margins matched the archived travel checks.
- Generated numerical results matched a fresh calculation from the input parameters.
- Authored local documentation links resolved.
- Nine unit tests passed, covering the nominal fit, excessive wire diameter, invalid turn counts, excessive travel, lead allowance effects, gravity, current/loss normalization and isolated FEMM run preparation.

These checks do not include a fresh FEMM solve, CAD-kernel reimport, Excel recalculation or physical testing. The geometry-validation JSON records prior CAD checks. The commissioning workbook records pending tests, not completed measurements.

Reproduce with the commands in the repository README. Recheck after changing inputs, calculations or source files.
