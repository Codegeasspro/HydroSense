# HydroSense

HydroSense is an experimental 3D-printed water-reservoir monitoring system using an ELEGOO UNO R3, an HC-SR04 ultrasonic sensor, a custom servo-driven tubing pinch valve, a Python hydraulic model and a live 3D digital twin.

**Status:** Preliminary design. No hardware testing or performance validation completed.

## Project boundaries

- Custom single-piece PETG reservoir with integrated hose outlet.
- External printed valve body/cam actuated by an existing SG90 servo.
- Level acquisition over USB serial; calibrated storage-volume computation.
- Model-based analysis of controlled water loss and discharge.
- Browser-based Three.js visualization updated from measurements.
- Additional materials budget ceiling: CAD $100.

A sensor measuring water level alone cannot distinguish a leak from intentionally released outlet flow without an independent measurement or model of expected discharge. The research protocol will make this distinction explicit.

## Getting started

Read [`docs/design-basis.md`](docs/design-basis.md) and [`docs/experimental-plan.md`](docs/experimental-plan.md). The first build step is a PETG watertightness test coupon and a parametric CAD model; production hardware is not yet designed.

## Repository layout

- `cad/source/`: editable FreeCAD files (forthcoming).
- `cad/printable/`: approved export meshes (forthcoming).
- `firmware/hydrosense_uno/`: Arduino acquisition firmware (forthcoming).
- `src/hydrosense/`: Python acquisition, hydraulics and analytics.
- `hardware/`: circuit, wiring and purchased-parts records.
- `experiments/`: test protocols, raw measurements and analysis.
- `tests/`: unit and model verification tests.

## Engineering model

For constant-area geometry: `V = A*h`, `h = H - d`, and `dV/dt = Q_in - Q_out - Q_leak`. All geometry values are preliminary until CAD and measurement verification.

## Safety

No pressure operation or potable-water use. Leak-test on a tray without electronics nearby. Keep the HC-SR04 and controller dry.

## License

License decision pending. Do not assume open-source reuse rights until a license is selected.
