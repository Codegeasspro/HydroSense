# Preliminary experimental plan

Revision 0.2, 2026-11-14. Targets are pre-registered design objectives, not measured performance.

## Research question

What is the minimum detectable abnormal water-loss rate in a low-cost instrumented reservoir under varying hydraulic head, sensor noise, calibration drift, and valve-discharge uncertainty?

HydroSense detects unexplained net water loss. It does not localize a physical leak or establish water quality or potability.

## Hypothesis and decision boundary

The physics-informed residual detector with declared uncertainty bounds will have lower false-positive frequency or lower detection latency than fixed level thresholds and adaptive CUSUM when tested against the same independent ground truth.

The controller has three advisory outputs:

1. `normal`: measurements are consistent with the hydraulic model.
2. `alert`: a residual exceeds the declared uncertainty threshold.
3. `indeterminate`: data quality or actuator-state evidence is insufficient for a defensible classification.

No automatic water-control action is permitted during the initial evaluation.

## Method

1. Establish the sensor-to-bottom datum and level-to-volume curve using independently measured water additions.
2. Quantify closed-outlet baseline, repeatability, drift, missing-data behaviour, and sampling latency.
3. Calibrate normal outlet discharge `Q_out(h, theta)` by collecting and weighing discharged water at selected hydraulic heads and valve positions.
4. Generate controlled abnormal losses using a separately calibrated loss path. Record collected mass and elapsed time as ground truth.
5. Run normal-discharge, abnormal-loss, sensor-bias, sensor-drift, spike, missing-data, and valve-model-error trials.
6. Partition trials into development and held-out evaluation sets before fitting detector settings.
7. Evaluate identical trials with fixed thresholds, rate-of-change thresholds, CUSUM, mass-balance residual, and uncertainty-aware residual methods.

## Model

For constant-area geometry, `V = A*h`, `h = H-d`, and:

`dV/dt = Q_in - Q_out - Q_loss`

The one-step predicted storage state is:

`V_predicted(t + Δt) = V_predicted(t) + (Q_in - Q_out) Δt`

The diagnostic residual is:

`r(t) = V_measured(t) - V_predicted(t)`

An alert may be issued only when the magnitude of `r(t)` exceeds a predeclared multiple of the propagated standard uncertainty. The source and magnitude of every uncertainty component must be recorded.

## Primary outcome

Define the minimum detectable loss rate, `Q_loss,min`, as the lowest independently measured abnormal-loss rate that reaches at least 90% sensitivity at a false-positive rate no greater than 5%, within a predeclared observation window. This definition must be applied to held-out trials.

## Secondary outcomes

- Depth mean absolute error and repeatability.
- Storage-balance closure error.
- Precision, recall, specificity, F1 score, and false-positive rate.
- Detection latency.
- Sensitivity to hydraulic head, sensor bias, drift, missing data, and valve-model error.
- Number of indeterminate outcomes.
- Calibration time, recalibration interval, and material cost.

## Data and provenance

Retain raw CSV files and metadata including trial identifier, timestamp, unit conventions, actual tank geometry, printed revision, sensor serial number, sensor calibration state, tube specifications, valve command, independently observed valve state, ground-truth mass collection, test condition, and rejection reason. Never overwrite raw data. Derived data and analysis outputs must cite their source files and software revision.
