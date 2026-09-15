# Project audit — current build versus recovered material

Audit date: 2026-09-15.

## Active engineering definition

The only active motor definition is [11-current-build.md](11-current-build.md), supported by the [one-rail BOM](12-one-rail-bom.md) and [current winding recipe](../winding-machine/docs/CURRENT_120T_AWG25_RECIPE.md): nine 120-turn AWG25 air coils on 8 mm centres; Ø10 × 5 mm N42SH discs paired into 10 mm sections; 2 mm steel spacers; 12 mm pitch; 12/11 mm carbon tube; 370 mm X coil-centre travel.

## Material retained as historical

The Rev62/Rev64 CAD, FEMM, calculations, manual, old BOM, visual GIF and winder parameters describe a different six-coil, 80-turn, 40 mm-stroke concept. They are retained for source recovery and comparison only. They must not be used as current manufacturing or electrical instructions.

## Withdrawn simulation claims

The prior Elmer motion study is withdrawn as a physical field/force model. Its coil geometry and rendered flux representation do not correctly model the active annular nine-coil pack. The GIF and image frames are therefore illustrative artefacts only. No force, back-EMF, heating, field-through-coil or motion claim may be inferred from them.

A replacement simulation must include an axisymmetric or 3-D geometry that correctly represents: the carbon tube, alternating axially magnetised discs, 2 mm spacers, annular coil cross-sections, all nine coil positions, phase currents, air domain and a validated material model. It must be checked against a physical static force test before being used for design ratings.

## Open work

1. Trial-wind one active 120-turn coil and record its bore, OD, width, resistance and mass.
2. Design the nine-coil carrier, end retention and lead exit from the measured coil.
3. Assemble a short magnet-stack sample and verify the spacer/clamping scheme.
4. Build a corrected FEM model from measured geometry, then correlate it with restrained force measurements.
5. Run the thermal test in the 70 C chamber and apply the 120 C provisional winding limit.
6. Verify the RLS encoder location remains below its field and temperature limits.

This audit does not discard recovered data; it prevents older assumptions from being mistaken for the live design.
