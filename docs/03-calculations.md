# Calculations and assumptions

> **Historical Rev64 reference — not the active build.** This file describes the recovered six-coil / 80-turn Rev64 concept. It does not define the current nine-coil prototype. Use [the current prototype definition](11-current-build.md), [one-rail BOM](12-one-rail-bom.md), and [project audit](13-project-audit.md) for active work.

Run `python tools/calculate.py` from the repository root to generate [results](../calculations/results.md) and [machine-readable values](../calculations/results.json). Inputs are in [parameters.json](../calculations/parameters.json). The calculator rejects impossible layer counts and gross overfill; passing those checks does not prove a manufacturable winding.

## Source hierarchy and units

Geometry comes from Rev64 CAD parameters and FEMM coordinates. Force comes from archived simulation CSVs. Wire dimensions and resistance per metre come from the linked Elektrisola IEC table. Extra lead length, procurement allowance, copper density and temperature coefficient are explicitly stated estimates. The historical mass and acceleration are workbook targets, not newly confirmed requirements. SI units are used for electromagnetic and dynamic equations; geometry uses mm with explicit conversions.

## Geometry

Let N_c be coil count, p coil pitch, w coil width, t bobbin wall and D_b bobbin bore.

- Stack length = 16 × 5 + 7 × 2 = 94 mm.
- Coil-pack length = (N_c − 1)p + w = 44 mm.
- Bobbin length = 44 + 2 × 0.5 = 45 mm.
- Coil ID = D_b + 2t = 13.4 mm.
- Radial window h = (16.8 − 13.4)/2 = 1.7 mm.
- Window cross-section = wh = 6.8 mm².
- Minimum winding end margin = 94/2 − 20 − 44/2 = 5 mm.
- Minimum bobbin end margin = 94/2 − 20 − 45/2 = 4.5 mm.
- Magnet-to-tube radial gap = (10.2 − 10)/2 = 0.10 mm.
- Tube-to-bobbin radial gap = (12.4 − 12)/2 = 0.20 mm.

For an annular component, V = π(D_o² − D_i²)L/4. Use D_i = 0 for a solid magnet disc. Bobbin volume equals the base sleeve plus the radial material above the base over the five 4 mm lands and two 0.5 mm flanges. Source component volumes are independently checked against these formulas.

## Winding fit

At finished wire diameter d_f = 0.281 mm, the ordered rectangular plan is 14 + 14 + 13 + 13 + 13 + 13 = 80 turns. Six layers occupy 6d_f = 1.686 mm radially. The widest layer occupies 14d_f = 3.934 mm axially. Nominal allowances are 0.014 mm radially and 0.066 mm axially.

The purely geometric diameter ceiling is min(1.7/6, 4/14) = 0.283333 mm, before any allowance. The specified 0.281 mm maximum is below that ceiling but only barely. Real crossovers, irregular stacking, enamel variation, bobbin tolerance and impregnation consume clearance. No extra insulation or adhesive allowance is built into the nominal fit.

Bare copper area A = πd_bare²/4 = 0.0490874 mm². Cross-sectional copper fill fraction = 80A/(4 × 1.7) ≈ 57.75%. This area fraction does not describe packing difficulty by itself. It also is not exactly the winding-volume fill when the turn counts vary by layer radius.

## Wire length, resistance and mass

For layer j starting at zero, centre diameter D_j = D_coil_ID + (2j + 1)d_f. Approximate turn length is πD_j. The model uses L_winding = Σ(n_j πD_j)/1000 metres. It neglects the tiny helical correction and excludes crossovers and terminals.

The explicit allowance is 0.20 m extra wire per coil. This is a planning input, not a recovered lead-routing dimension. Total wire per coil = L_winding + allowance. Production consumption is six times that value. A separate 20% procurement allowance is applied only to purchase length, not electrical resistance or copper mass. One trial coil adds its own consumption before that allowance.

R_coil,20 = wire length × 0.3482 Ω/m. The supplier table's 0.3345–0.3628 Ω/m range produces an estimated resistance band for the same length. Each series phase has two coils, so R_phase = 2R_coil, plus any extra interconnect resistance not included in the allowance. For a balanced star connection measured between two terminals with the third open, R_line-line = 2R_phase. These relations do not apply unchanged to delta wiring.

Copper mass = A × length × density after unit conversion. Density 8.9 g/cm³ is an estimate. Insulation, solder, lead dress, bobbin, carriage and adhesive are excluded. Bobbin CAD volume is available, but bobbin mass remains V × selected-material density. Total moving mass is unavailable until the mechanical BOM is specified.

## Force and current definitions

For phase permanent-magnet flux linkages λ_A, λ_B, λ_C in Wb-turn and displacement x in metres, define g = dλ/dx. Remove the common-mode component: p = g − mean(g)[1,1,1]. Then K = ||p||₂ and u = p/K. The optimum balanced current is i = I_vector u, satisfying sum(i) = 0 and ||i||₂ = I_vector. Its PM force prediction is F = g·i = K I_vector.

The archived script uses centred differences at interior samples and one-sided differences at ±20 mm. Displacement spacing is 0.25 mm. These gradients and normalized currents are checked again from the saved flux data.

For the conventional balanced sinusoidal scaling, I_vector = sqrt(3/2) I_phase_peak, and each phase RMS over a sinusoidal cycle is I_phase_peak/sqrt(2). Therefore K_phase_peak_equivalent = sqrt(3/2) K. The saved optimum vectors are not a guarantee that an arbitrary fixed sinusoidal commutation law produces the same force. At standstill, the individual DC phase values differ from their over-cycle RMS values. Always state which current convention is used.

Direct-force validation uses F_PM_odd = [F(+i) − F(−i)]/2 and F_even = [F(+i) + F(−i)]/2. Relative difference = 100(F_PM_odd − K)/K for the saved unit-vector currents. Three checks are consistency evidence, not a full mesh-convergence study or measured force map.

## Copper loss and temperature

For equal phase resistance R_phase and arbitrary instantaneous currents, P_copper = R_phase(i_A² + i_B² + i_C²) = R_phase I_vector². Under equivalent sinusoidal phase-peak scaling this becomes 1.5 R_phase I_phase_peak². Current scenarios in the generated table are arithmetic examples, not approved operating limits.

R(T) = R20[1 + α(T − 20°C)], using α = 0.00393/K as an estimate. A measured reference at T_ref gives T = 20 + {(R/R_ref)[1 + α(T_ref − 20)] − 1}/α. Measure after settling and account for lead/contact resistance. This estimates average copper temperature, not the hottest turn.

At thermal steady state, Rθ ≈ (T − T_ambient)/P. With equal phase resistances, a provisional current calculation would be I_phase_peak ≤ sqrt[(T_limit − T_ambient)/(1.5 R_phase(T_limit) Rθ)]. Rθ, ambient worst case, material-compatible T_limit and duty cycle are missing, so no continuous-current result is assigned. The old 120°C workbook entry is not an approved limit.

## Load, acceleration and orientation

Historical targets give F_inertia = ma = 0.5 × 5.186 = 2.593 N. A vertical upward acceleration requires F = m(a + g) + friction + external load; with gravity alone added, F = 7.496325 N. Horizontal force ignores gravity along the axis but still needs friction and cable load. The generated estimates divide these loads by the minimum archived K to show conservative position-based current within this first-pass simulation. They do not include a design margin or magnetic-temperature derating.

Holding force on a vertical axis is mg even at zero acceleration. A commanded current failure cannot be treated as a holding brake. Orientation must be confirmed before accepting an operating envelope.

## Back EMF, voltage and missing dynamic calculations

For each phase, e_j = (dλ_j/dx)v. The relevant line voltage is e_A − e_B, etc. The generated results report the largest absolute saved phase and line gradient, which give voltage per m/s. Multiplying the projected force constant by velocity does not automatically give a phase-to-phase back-EMF value.

General phase voltage is v = Ri + d(Li)/dt + e_PM, with mutual terms in the inductance matrix and position dependence if present. A first current-ramp estimate is di/dt ≈ (V_available − Ri − e)/L only after defining the electrical circuit and inductance. The 12 mm adjacent-pair pitch implies a nominal 24 mm magnetic period, so f_e ≈ |velocity|/0.024 m away from end effects. Full force commutation should use a calibrated position/phase map.

Inductance matrix, bus voltage, maximum speed, PWM ripple, eddy losses, saturation, magnetic temperature effects, fatigue life, structural deflection and a thermal duty rating cannot be calculated numerically from the supplied evidence. Required inputs and tests are listed in the roadmap; no guessed values are presented as results.

