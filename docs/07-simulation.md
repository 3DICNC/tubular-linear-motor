# Simulation and reproduction

## Archived model

The preserved Rev64 FEMM file is a static axisymmetric model in millimetres with precision 1e−8, a zero-vector-potential outer boundary and an approximately r = 0–30 mm, z = −60–60 mm air domain. All six coils are group 100. Their radii are 6.7–8.4 mm and their centres are −20, −12, −4, 4, 12, 20 mm. The saved starting phase currents are −1, +0.5, +0.5 A; the sweep resets them to zero.

| Material | Saved model assumption |
|---|---|
| Air and implicit bobbin | Relative permeability 1 |
| CarbonTube | Relative permeability 1, conductivity 0 |
| Steel_firstpass | Constant relative permeability 1000, no B–H points |
| N42SH_firstpass | Relative permeability 1.05, coercive field 1,000,000 A/m |
| Copper | Conductivity 58 MS/m; no explicit individual-wire geometry |

The magnetic material label is not a verified supplier material curve. The model omits thermal feedback, real steel saturation, magnet temperature dependence, PWM and conductive carbon-tube losses. Treat winding resistance from physical wire geometry and measurements separately from a homogenized coil-region solution.

## What the archived sweep does

It translates the whole coil group through 161 positions at 0.25 mm increments over ±20 mm, extracts zero-current PM circuit flux linkages, differentiates them and calculates balanced optimum current vectors. It then solves positive and negative currents at −20, 0 and +20 mm and integrates axial Lorentz force on all six coil regions.

FEMM `mo_blockintegral(12)` is the steady-state axial Lorentz-force component for an axisymmetric magnetic model. The official [FEMM manual](https://www.femm.info/Archives/doc/manual.pdf) documents the integral and circuit-property APIs. The air-like coil permeability makes this force calculation appropriate for the coil regions.

The saved direct-force comparisons are within 0.35%; the largest even component is about 0.000059 N. Recalculation of saved data is not a new finite-element solve. Archived CAD-kernel reimport checks are also preserved evidence, not rerun by the documentation tools.

## Fresh runs without overwriting the archive

The preserved Lua uses absolute paths from its original computer location. Do not run it in place. Instead:

```sh
python tools/prepare_femm.py --output work/femm-trial-01
```

The tool creates a new directory, copies the centred model, adapts only the input/output paths in a copied Lua script, and removes automatic application exit. It refuses an existing output directory. Open FEMM and use its Lua script command to select the generated script. The script creates new CSVs inside the run directory. The original simulation directory stays untouched.

Do not apply the older −36 mm translation to this already-centred model. Wait for the run's `progress.txt` to report completion. Archive the new model, outputs, solver version and machine/run notes together. The run preparation tool has been checked for file isolation; the resulting Lua has not been executed as part of this documentation task.

## Before treating force as a release value

Perform mesh refinement and air-boundary sensitivity studies, compare central and endpoint differentiation schemes, add supplier magnetic curves and temperature cases, check proposed metal fixtures, measure force at known phase currents and positions, and resolve the actual drive's commutation law. Losses and dynamics require additional models and measurements. Model convergence at a numerical precision setting alone does not establish physical accuracy.
