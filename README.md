# HydroSense

HydroSense is an experimental, low-cost hydraulic testbed for studying detection of abnormal water loss in an instrumented reservoir. The platform couples a 3D-printed PETG reservoir, level and flow measurement, an SG90-driven pinch valve, a physics-informed mass-balance model, and transparent fault-aware detection benchmarks.

**Status:** Preliminary design and software benchmark stage. No hardware test, sensor calibration, leak-detection result, or material-performance claim has been validated.

## Project boundaries

- Custom single-piece PETG reservoir with integrated hose outlet.
- External printed valve body/cam actuated by an existing SG90 servo.
- Level acquisition over USB serial; calibrated storage-volume computation.
- Model-based analysis of controlled water loss and discharge.
- Independently measured discharge, controlled-loss experiments, and a documented ground-truth method.
- Comparison of fixed-threshold, CUSUM, mass-balance residual, and uncertainty-aware residual detectors.
- Advisory-first decision logic: normal operation, anomaly alert, or indeterminate result. Automatic actuation is out of scope until detector performance is demonstrated.
- Additional materials budget ceiling: CAD $100.

A sensor measuring water level alone cannot distinguish a leak from intentionally released outlet flow without an independent measurement or model of expected discharge. HydroSense therefore investigates unexplained net water loss, not physical leak location. It does not assess potable-water safety or replace certified water-monitoring instrumentation.

## CAD files

Open `models/HydroSense_Integrated_V2.FCStd` in FreeCAD for the assembled design. The editable reservoir feature history is in `models/HydroSense_Reservoir_V2_constrained.FCStd`. Printable meshes are in `exports/`.

See [ENGINEERING_DESIGN.md](ENGINEERING_DESIGN.md) for geometry, engineering checks, snap-fit interfaces, test limits, and the preliminary versus validated distinction. The research basis and experiment design are in [`docs/research-gap.md`](docs/research-gap.md) and [`docs/experimental-plan.md`](docs/experimental-plan.md). The BOM is a planning input only; it must be repriced in CAD before claiming compliance with the CAD $100 incremental-materials cap.

## Repository layout

- `models/`: editable `.FCStd` files.
- `exports/`: generated printable STL files.
- `firmware/hydrosense_uno/`: Arduino acquisition firmware (forthcoming).
- `src/hydrosense/`: Python hydraulic model and detection benchmarks.
- `hardware/`: circuit, wiring and purchased-parts records.
- `experiments/`: test protocols, raw measurements and analysis.

## Engineering model

For constant-area geometry: `V = A*h`, `h = H - d`, and `dV/dt = Q_in - Q_out - Q_loss`. All geometry values are preliminary until CAD and measurement verification. The primary residual is `r = V_measured - V_predicted`; it is interpreted only with a declared uncertainty model and independently recorded ground truth.

## Safety

No pressure operation or potable-water use. Leak-test on a tray without electronics nearby. Keep the HC-SR04 and controller dry.

## License

License decision pending. Do not assume open-source reuse rights until a license is selected.
