# Preliminary design basis

Revision 0.2, 2026-11-14. All parameters are unvalidated.

| Item | Proposed value |
| --- | --- |
| Internal length | 140 mm |
| Internal width | 100 mm |
| Internal height | 160 mm |
| Operating depth | 120 mm (pending sensor clearance) |
| Nominal operating volume | 1.68 L |
| Tank | PETG, single-piece FDM print |
| Outlet | Integral hose barb, separately leak-tested |
| Valve | External cam-type SG90 pinch valve with flexible silicone tubing |
| Sensor | HC-SR04 above water, verified measurement range required |
| Flow reference | Independently calibrated inline sensor or gravimetric collection method |
| Primary research output | Minimum detectable abnormal loss rate under declared uncertainty |

**Design holds:** Confirm actual printer build volume, sensor working range, tube ID/OD, actuator torque, nozzle geometry, sealing test method, PETG availability, outlet calibration method, ground-truth loss method, and uncertainty budget before production print.

Calculations: area = 0.140 × 0.100 = 0.0140 m²; volume at 0.120 m depth = 0.00168 m³; hydrostatic base pressure = 1000 × 9.81 × 0.120 = 1177.2 Pa. Hydrostatic pressure alone does not establish structural strength or leak integrity.

The tank is a controlled bench-scale research asset. It is not a pressure vessel, certified water-storage product, potable-water device, or representation of a municipal distribution network.
