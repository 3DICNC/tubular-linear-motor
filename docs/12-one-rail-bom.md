# One-rail bill of materials — X-axis reference

This BOM is for one complete 370 mm-travel motor rail. It is the purchase and build reference for the first X-axis prototype, not the total printer quantity. The twin Y rails need two matched copies of the magnet, tube, coil and encoder items, with 500 mm encoder scales.

| ID | Item | Qty to buy | Per rail used | Specification / decision |
|---|---|---:|---:|---|
| MAG-10-5 | N42SH disc magnet | 80 | 78 | 10 mm diameter x 5 mm thick, axial magnetisation, 150 C minimum, same supplier batch. Build 39 two-disc magnetic sections; retain 2 as spares. |
| SP-10-8-2 | Low-carbon steel spacer | 40 | 38 | 10 mm OD x 8 mm ID x 2 mm. Flat, burr-free carbon-steel washer or laser-cut shim; retain 2 spares. |
| TUBE-12-11 | Carbon tube | 1 x 500 mm | 1 x about 480 mm | 12 mm OD x 11 mm ID; do not final-cut until stack retention is proven. |
| END-RET | End-retention set | 2 | 2 | Custom nonmagnetic end plugs/retainers and assembly fixture. Design still required. |
| COIL-120 | Air coil | 9 | 9 | 13 mm bore x 5 mm wide, 120 turns, 8 mm centre pitch. |
| WIRE-AWG25 | Enameled copper wire | 100 m spool | 67.5 m nominal | AWG25 / 0.455 mm bare, about 0.496 mm finished, Class F minimum. Prepare 7.5 m per coil. |
| RESIN-EL160 | Impregnation resin | 1 kit | as needed | Easy Composites EL160; user has ordered this. Follow its cure and post-cure schedule. |
| CARRIER-9C | Nine-coil carrier | 1 | 1 | Custom nonmagnetic coil support and lead exit; CAD release pending after a physical coil trial. |
| RAIL-MGN12H | Linear guide | 1 | 1 | 450 mm MGN12H rail with carriage, aligned independently from the motor tube. |
| ENC-RLS | Linear encoder readhead | 1 | 1 | RLS `RLC2HDAD20B00C00`, 5 V TTL A/B/Z, 10 um resolution. |
| SCALE-RLS | Magnetic encoder scale | 1 | 1 | RLS `MS05AM450B0000`, 450 mm. |
| FOIL-RLS | Scale cover foil | 1 | 1 | RLS `CF050045`, 450 mm. |
| ENC-HARNESS | Encoder cable | 1 | 1 | Lightweight shielded five-core flexible cable: 5V, GND, A, B, Z. Keep away from motor phase wires. |
| TEMP-COIL | Coil temperature sensor | 1 | 1 | Fine Type-K thermocouple embedded on the outer surface of the centre coil before impregnation. |
| TEMP-TUBE | Tube temperature sensor | 1 | 1 | Fine Type-K thermocouple bonded to the carbon tube just beyond the coil pack; indirect magnet-temperature indication. |
| DRIVE | Motor controller channel | 1 | 1 | One MKS XDrive 3.6 channel at 48 V. The board may serve a second rail on its other channel. |
| BRAKE | Braking resistor | 1 | 1 | Sized after supply and regenerative-energy validation; required before high acceleration testing. |

## Assembly count check

- 39 sections x 2 magnets = 78 fitted magnets.
- 39 sections create 38 inter-section gaps = 38 fitted steel spacers.
- Stack length = 39 x 10 mm + 38 x 2 mm = 466 mm.
- Nine coils x 7.5 m prepared wire = 67.5 m; a 100 m spool covers winding, leads and a trial coil.

## External links

- [RLS RLC2HD product and configurator](https://www.rls.si/eng/rlc2hd-miniature-linear-and-rotary-pcb-level-incremental-magnetic-encoder?partNumbers=RLC2HDAD20B00C00&readingTypeOptionIds=8762)
- [RLC2HD data sheet](https://cdn.rls.si/documents/datasheets/RLCD03_09_RLC2HD_datasheet_.pdf)
- [RLS MS magnetic scales](https://www.rls.si/eng/ms-scale)
- [ODrive incremental encoder wiring](https://docs.odriverobotics.com/v/latest/manual/hardware-config.html)
- [Makerbase ODrive/XDrive hardware repository](https://github.com/makerbase-motor/MKS-ODrive)
- [EL160 high-temperature laminating resin](https://www.easycomposites.eu/el160-high-temperature-epoxy-laminating-resin)

No magnet supplier is named here because stock and batch availability are still being confirmed. Order only after the supplier confirms N42SH (or an approved equivalent), axial magnetisation, 150 C working temperature and a single production batch for every magnet needed on the same rail.
