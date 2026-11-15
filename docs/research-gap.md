# Research gap and contribution

## Problem statement

Low-cost reservoir monitors commonly trigger an alarm from water level alone. A reduction in level can result from intended discharge, unplanned loss, sensor drift, sensor noise, incorrect geometry, actuator error, or missing data. A level-only system therefore cannot establish that a leak has occurred.

HydroSense investigates the reliability boundary of low-cost hydraulic anomaly detection in a controlled single-reservoir system. The study asks when an unexplained net loss can be detected, rather than claiming municipal-network-scale leak localization or water-quality certification.

## Research question

What is the minimum detectable abnormal water-loss rate in a low-cost instrumented reservoir under varying hydraulic head, sensor noise, calibration drift, and valve-discharge uncertainty?

## Contribution

HydroSense will provide an open, reproducible bench-scale dataset and benchmark that combines:

- a parametric, low-cost physical reservoir;
- calibrated level-to-volume and valve-discharge measurements;
- independently measured controlled-loss ground truth;
- fault injections for bias, drift, spikes, missing data, and valve-model error;
- fixed-threshold, CUSUM, mass-balance residual, and uncertainty-aware residual detectors; and
- predeclared performance measures, including detection sensitivity, false-positive rate, latency, and minimum detectable loss rate.

The platform is advisory-first. Automatic actuation is not a success criterion until detection performance and failure modes have been characterized.

## Literature position

Ruiz-Diaz et al. identify shortcomings in real-world validation, cross-network generalization, comparability, and availability of practical data in smart leak-detection research. Their D-A-T taxonomy will be used to classify HydroSense as hydraulic sensing, local/edge processing, and leak or abnormal-loss detection rather than localization [1].

Masoudimoghaddam et al. demonstrate that low-cost ultrasonic water-level sensing can be evaluated with laboratory and field validation. HydroSense will reproduce the methodological principle of reporting device-specific calibration and error, without transferring the reported performance of another sensor directly to its own hardware [2].

Ghorbani Bam et al. distinguish synchronized, feedback-capable digital twins from static models and dashboards. HydroSense will retain the term digital twin only if live state synchronization, calibrated model updating, transparent uncertainty treatment, and traceable decision logic are implemented [3].

Steins et al. present an adaptive, nonparametric CUSUM detector robust to noisy and non-normal monitoring data. HydroSense will implement CUSUM as a benchmark against which its physical mass-balance residual detector is evaluated [4].

## Scope exclusions

- Potable-water safety assessment or contaminant identification.
- Physical leak localization.
- Unvalidated control of safety-critical infrastructure.
- Unqualified extrapolation from the tank to a municipal network.
- Claims of field readiness before long-duration tests and independent replication.

## References

1. Ruiz-Diaz, J.; Ruiz-Vanoye, J. A.; Trejo-Macotela, F. R.; et al. Smart Leak Detection in Water Distribution Networks: A Systematic Review and D-A-T Taxonomy. *Water* 2026, 18, 2797. https://doi.org/10.3390/w18212797.
2. Masoudimoghaddam, S.; Yazdi, J.; Shahsavandi, N. A Low-Cost Ultrasonic Sensor for Online Monitoring of Water Levels in Rivers and Channels. *Flow Measurement and Instrumentation* 2025, 102, 102777. https://doi.org/10.1016/j.flowmeasinst.2024.102777.
3. Ghorbani Bam, P.; Rezaei, N.; Roubanis, A.; et al. Digital Twin Applications in the Water Sector: A Review. *Water* 2025, 17, 2957. https://doi.org/10.3390/w17202957.
4. Steins, E.; Langer, N.; Koslowski, J.; Cominola, A. From Theory to Practice: Robust and Automated Data-Driven Leakage Detection in Water Distribution Networks. *Journal of Water Resources Planning and Management* 2026, 152. https://doi.org/10.1061/JWRMD5.WRENG-7401.
