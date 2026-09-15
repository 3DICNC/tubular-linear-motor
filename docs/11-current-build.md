# Current prototype build definition

This chapter is the active build definition. It supersedes the recovered Rev62/Rev64 dimensions wherever they disagree. The recovered packages remain historical evidence and must not be treated as the present manufacturing drawing.

## One moving-coil motor rail

The first rail is the X-axis unit. It provides 370 mm usable coil-centre travel for a 355 mm bed. The Y axis uses the same motor architecture on two matched rails, with 440 mm usable travel each.

| Feature | Active definition |
|---|---|
| Magnet rod | 39 magnetic sections; 466 mm active stack length |
| Magnetic section | Two axially magnetised 10 x 5 mm N42SH discs, joined N-to-S |
| Separator | 38 low-carbon-steel spacers, 10 mm OD x 8 mm ID x 2 mm; adjacent sections face the same pole across each spacer |
| Magnetic pitch | 12 mm section-to-section centre pitch |
| Tube | Carbon fibre, 12 mm OD x 11 mm ID; buy 500 mm and trim only after the stack and end retention are proven |
| Coil pack | Nine independent air coils, 8 mm centres, 69 mm overall axial length |
| Coil | 13 mm bore, 5 mm axial width, 120 turns AWG25 enamelled copper |
| Wire | 0.455 mm bare / about 0.496 mm finished; about 7.5 m prepared per coil |
| Phase order | A-B-C-A-B-C-A-B-C; three series coils per phase |
| Resin | Easy Composites EL160, with the maker's specified post-cure |
| Controller | One channel of MKS XDrive 3.6 at 48 V; a braking resistor is required for regeneration |

The current N42SH grade is essential for the 70 C heated chamber. Standard N52 is normally limited to about 80 C and is not an acceptable final motor magnet without a temperature rating from its manufacturer. Every magnet on a rod must come from the same grade and supplier batch. The two Y rods must be matched as a pair.

## Preferred encoder

The preferred feedback system is the RLS RLC2HD linear incremental encoder with a separate RLS MS05 magnetic scale. It is deliberately mounted on the rail side of the machine, away from the tubular motor magnet rod.

| Item | Selected part / setting |
|---|---|
| Readhead | `RLC2HDAD20B00C00` |
| Interface | 5 V single-ended TTL A, B and Z incremental signals |
| Resolution | 10 um (`D20`, 200 interpolation factor) |
| Edge separation | 0.5 us / 2 MHz (`B`) |
| Connector | No connector (`00`); solder a light flexible harness |
| Reference | Periodic reference every 2 mm (`C`) |
| X scale | `MS05AM450B0000`, 450 mm long, plus `CF050045` cover foil |
| Y scales | Two 500 mm MS05 scales and matching 500 mm cover foils; confirm final part numbers in the RLS configurator |

At 10 um, one 12 mm magnetic pitch contains roughly 1,200 encoder position increments. That is ample for force commutation; choosing 1 um would create ten times more pulses with no practical force or print-accuracy benefit. The selected readhead is directly compatible with the 5 V A/B/Z header on an MKS XDrive 3.6 / ODrive v3.6-style controller: connect 5V, GND, A, B and Z one-for-one. No EIA-422 converter is needed.

RLS specifies -30 to +85 C operation and permits less than 1 mT external field at the scale/readhead. The readhead and scale must therefore sit outside the motor's stray field and should not be installed inside the 70 C heated volume. Verify field and temperature at the final mount before relying on the encoder.

## Heat and operating limit

The 70 C-chamber thermal screen predicts approximately 142.5 C winding temperature after 30 minutes for the original 0.792 W-per-coil repeated-motion case. This is too close to Class-F wire insulation (155 C). Until the physical thermal test is complete, use a conservative 120 C winding limit and the 0.55 W-per-coil continuous design case. Coil liquid cooling is an option, but any metallic heat spreader around the moving coils must be slotted to avoid eddy-current drag.

## Required verification before full build

1. Confirm magnet grade, axial magnetisation and Br range on the supplier certificate.
2. Trial-wind and impregnate one 120-turn coil; measure bore, OD, width and resistance.
3. Prove that the coil carrier moves freely on the 12 mm tube before winding all nine coils.
4. Build and clamp a short magnet-stack trial before assembling the full 466 mm rod.
5. Verify the RLS scale/readhead stays below 1 mT and 85 C in its final rail-side position.
6. Establish current, phase polarity, force map and thermal duty with restrained tests before fitting the printer.
