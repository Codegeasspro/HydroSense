# HydroSense

HydroSense is an experimental 3D-printed water-reservoir monitoring system using an ELEGOO UNO R3, an HC-SR04 ultrasonic sensor, a custom servo-driven tubing pinch valve, a Python hydraulic model and a live 3D digital twin.

**Status:** Preliminary design. No hardware testing or performance validation completed.

## Project boundaries

- Custom single-piece PETG reservoir with integrated hose outlet.
- External printed valve body/cam actuated by an existing SG90 servo.
- Level acquisition over USB serial; calibrated storage-volume computation.
- Model-based analysis of controlled water loss and discharge.
- Browser-based Three.js visualization updated from measurements.
- Additional materials budget ceiling: US$100.

A sensor measuring water level alone cannot distinguish a leak from intentionally released outlet flow without an independent measurement or model of expected discharge. The research protocol will make this distinction explicit.

## CAD files

Open `models/HydroSense_Integrated_V2.FCStd` in FreeCAD for the assembled design. The editable reservoir feature history is in `models/HydroSense_Reservoir_V2_constrained.FCStd`. Printable meshes are in `exports/`.

See [ENGINEERING_DESIGN.md](ENGINEERING_DESIGN.md) for geometry, engineering checks, snap-fit interfaces, test limits, and the preliminary versus validated distinction. The materials plan is in `BOM.csv` and totals US$79.00.

## Repository layout

- `models/`: editable `.FCStd` files.
- `exports/`: generated printable STL files.
- `firmware/hydrosense_uno/`: Arduino acquisition firmware (forthcoming).
- `src/hydrosense/`: Python acquisition, hydraulics and analytics.
- `hardware/`: circuit, wiring and purchased-parts records.
- `experiments/`: test protocols, raw measurements and analysis.

## Engineering model

For constant-area geometry: `V = A*h`, `h = H - d`, and `dV/dt = Q_in - Q_out - Q_leak`. All geometry values are preliminary until CAD and measurement verification.

## Safety

No pressure operation or potable-water use. Leak-test on a tray without electronics nearby. Keep the HC-SR04 and controller dry.

## License

License decision pending. Do not assume open-source reuse rights until a license is selected.
