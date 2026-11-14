# Preliminary experimental plan

## Question

What is the smallest controlled additional loss rate detectable by a low-cost ultrasonic reservoir monitoring system at a defined false-positive rate?

## Method

1. Establish sensor-to-bottom datum and usable range; record known depths and water volumes.
2. Measure closed-outlet baseline and drift with timestamped sensor readings.
3. Run controlled discharge trials; independently measure collected water and elapsed time.
4. Calibrate Q(h, theta) for the printed pinch valve under selected heads.
5. Introduce uncommanded loss relative to a known outlet baseline.
6. Evaluate detection latency, sensitivity, false positive fraction, rate error and repeatability using held-out trials.

## Key model

For constant-area tank, V = A*h, h = H-d, dV/dt = Qin-Qout-Qleak. The sensor measures total water loss, not the location or mechanism of that loss.

## Preliminary performance targets

Depth MAE <= 5 mm in calibrated range; balance closure within 5%; detector sensitivity >=90% and false-positive trial fraction <=10% for a predeclared rate range; digital twin displayed level update within 2 seconds of accepted data receipt. Targets are not verified performance.

Retain raw CSV and metadata including fluid depth, printed revision, actual geometry, tube specifications, valve angle, timestamps and sample rejection reasons.
