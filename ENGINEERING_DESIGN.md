# HydroSense V2 engineering design record

## Design basis

The recovered FreeCAD model is retained as `models/HydroSense_Reservoir_V1_original.FCStd`. Its outer and inner rectangle sketches had correct nominal dimensions but were underconstrained. `models/HydroSense_Reservoir_V2_constrained.FCStd` corrects them as centred, fully constrained sketches while retaining the editable PartDesign Pad and Pocket history.

| Feature | Design value | CAD verification status |
|---|---:|---|
| External tank envelope | 148 x 108 x 165 mm | Validated by FreeCAD kernel test |
| Internal pocket | 140 x 100 x 160 mm | Validated by sketch dimensions and 5 mm base |
| Side walls | 4 mm | Validated from centred 140 x 100 pocket |
| Base | 5 mm | Validated from 160 mm pocket depth |
| Nominal water capacity | 2.240 L | Derived from 140 x 100 x 160 mm cavity |
| Outlet bore | 10 mm ID | Validated CAD geometry |
| Outlet hose tail | 12 mm nominal OD with two ridges | Validated CAD geometry |

The 148 x 108 x 165 mm envelope is the tank body. The integrated hose tail projects 24 mm below the base and is not included in that envelope.

## Printable design

`models/HydroSense_Integrated_V2.FCStd` contains six editable solids and a parameter spreadsheet. It contains:

- a PETG tank with a reinforced bottom outlet, 16 mm OD boss, 10 mm through-bore, and 12 mm hose-tail;
- a perimeter base tray that supports the tank by gravity, keeps the outlet clear, and carries the valve dock;
- an HC-SR04-compatible sensor plate with two 16.4 mm apertures at 26 mm pitch, board tabs, and a 4.6 mm U-channel that snaps over the 4 mm tank rim;
- an open SG90 cradle with a 24.5 x 13.5 mm clearance envelope, a 6.6 mm ID split tube clip, and no added fasteners;
- a separate pinch arm with a 15 mm effective pivot-to-shoe radius.
- a removable PETG SG90 snap retainer that locks over the cradle rails.

The sensor clip, servo retainer, and tube clip are the no-added-fastener interfaces. The valve slides laterally onto the base tray's 18/12 mm male dovetail. Its mating groove has 0.6 mm clearance for PETG. The valve body also snaps onto the 6 mm silicone tube. This prevents servo or hose loads from concentrating at the reservoir outlet. The stock SG90 horn and its supplied centre screw remain necessary to transmit torque from the servo spline to the printed pinch arm.

Exported STLs are in `exports/`. Print the tank upright with the outlet facing the build plate only if the printer can bridge the bore cleanly. A safer default is tank upright with support at the outlet, four walls, 0.20 mm layers, and PETG. Print the mount, valve body, and arm flat. Use a 0.2 mm clearance test coupon before committing to a full print.

## Design checks

### Hydrostatic load

At the maximum 160 mm water depth:

\[
p_{base}=\rho g h=(1000)(9.81)(0.160)=1.57\ \mathrm{kPa}
\]

\[
V=(0.140)(0.100)(0.160)=0.002240\ \mathrm{m^3}=2.240\ \mathrm{L}
\]

Full water mass is approximately 2.24 kg. The static base load is 22.0 N. The design provides a 5 mm base and 4 mm walls. This is a preliminary geometry and static-load check. It is not a pressure-vessel qualification, leak qualification, or long-term PETG creep assessment.

### Servo pinch force

Using an assumed SG90 nominal stall torque of 1.8 kgf cm:

\[
T=1.8(0.09807)=0.1765\ \mathrm{N\,m}
\]

At the 15 mm effective arm radius, the nominal ideal pinch force is:

\[
F=T/r=0.1765/0.015=11.8\ \mathrm{N}
\]

A 50 percent derating for servo variability, friction, and continuous-duty avoidance gives a preliminary available force of 5.9 N. This is not enough evidence to claim tube closure. The valve is a preliminary concept until a 6 mm OD silicone tube is cycled with water and residual flow is measured. If it leaks, use a metal-geared servo, shorten the radius, or add a cam and hard pinch anvil.

### Material budget

The incremental-materials budget in `BOM.csv` is US$79.00, including 0.7 kg of PETG and a US$20 contingency. It satisfies the US$100 cap. The PETG allowance covers approximately 0.59 kg calculated from the six CAD solid volumes at 1.27 g/cm³. Prices are planning allowances, not purchase quotes.

## Validation and required bench tests

Validated now: FreeCAD solids are valid, the two reservoir sketches are fully constrained, the specified tank dimensions are met, the positioned tray, sensor clip, and valve have no solid interference, and six non-empty STL files were exported.

Required before water-service approval:

1. Dimensional inspection of a first article. Verify wall, base, outlet bore, 4.6 mm rim-clip gap, 6.6 mm tube-clip ID, 18/12 mm dovetail fit, and servo-retainer rail fit after PETG cooling.
2. Fill test at 2.24 L for 24 hours on a tray. Inspect the outlet boss and layer lines for leakage.
3. Cycle the servo at least 500 open-close cycles with the actual tube. Record residual flow, servo temperature, and gear backlash.
4. Confirm sensor readings at empty, half-full, and full states with the chosen sensor and controller. The supplied mount assumes an HC-SR04-compatible board and is not validated for submerged operation.
