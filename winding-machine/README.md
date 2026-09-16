# Automatic coil winder — active build

This folder holds the hardware work for the coil winder. The **active plan** is a two-stepper machine for the current tubular-motor coils:

- one NEMA17 and driver turn the removable winding mandrel;
- one NEMA17 and driver move the wire guide on the **2 mm-pitch threaded rod**;
- the MKS controller and existing software provide spindle speed, turn count and guide synchronisation;
- no servo, belt reduction, bevel gear, mechanical reversing gear or electrical control design is required for this build.

## What the winder must produce

The target is one independent air coil with a 13 mm bore, 5 mm axial winding width, 120 turns of AWG25 copper (0.455 mm bare, about 0.496 mm finished). The motor uses nine matched coils per rail.

Use [the active winding recipe](docs/CURRENT_120T_AWG25_RECIPE.md) and [the trial record](../records/winding-trial.md). Wind one slow test coil first; its measured dimensions determine the final guide pitch and the design of the motor coil carrier.

## Hardware still required

1. Rigid base, spindle bearings, 13 mm removable mandrel and a simple non-magnetic end stop.
2. Wire-guide carriage driven by the 2 mm-pitch rod, with adjustable tensioner and smooth ceramic/metal eyelet.
3. Two NEMA17 motors, drivers and MKS control board already available to you.
4. Guard around rotating components, accessible emergency stop and a wire-break stop before normal operation.

## Historical files

The `rev_b_gt2`, `rev_c_printed_gears`, older CAD, old BOM and mechanical-reduction documents are retained as concept history. Their original Rev64 coil assumptions were 80 turns of 0.250 mm wire and must not be used for the active winding recipe. `legacy_rev64_winding_parameters.json` preserves those old values.

No current STEP manufacturing assembly is released yet because the spindle/mandrel dimensions need the first physical 13 mm coil trial. The existing hardware concepts can be adapted after that measurement.
