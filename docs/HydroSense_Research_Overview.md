# HydroSense: Research concept and prototype overview

*Companion to the six-page author-supplied `Hydrosense_Overview(1).docx` (November 2026). The Word original includes apparatus/workflow figures and FreeCAD orthographic views not reproduced here. Design remains preliminary and unvalidated.*

HydroSense is a proposed low-cost laboratory platform for investigating the reliability of water-balance-based abnormal-loss detection. It combines a custom 3D-printed reservoir, ultrasonic level measurements, controlled discharge and a physics-informed computational model. The immediate objective is to quantify detection limits under measurement and model uncertainty; future applications may include reproducible laboratory research and monitoring small water-storage installations.

## Research motivation

A declining reservoir level establishes a change in stored water, not the cause. Controlled withdrawals, evaporation, sensor bias and discharge-model error can resemble unintended leakage. The central hydrological inference and observability problem is identifying which terms of a water balance are estimable from limited and uncertain observations.

The proposed testbed will provide known hydraulic boundary conditions and independent ground-truth measurements. A valuable research contribution would be a reproducible experimental benchmark showing both successful detections and conditions under which detection is unreliable.

## Proposed research question

Under varying hydraulic head, outlet operation, sensor uncertainty and discharge-model error, what is the minimum additional water-loss rate that a low-cost physics-informed monitoring system can detect at a specified false-alarm rate?

Working hypotheses:

1. A calibrated storage-and-discharge model will yield fewer false alarms than a simple level threshold during normal valve operations.
2. Measurement and model uncertainty will constrain the minimum detectable additional loss.
3. Longer observation windows will improve sensitivity to smaller losses but increase detection delay.

These are testable hypotheses, not established outcomes.

## Proposed apparatus and methods

| Element | Preliminary specification |
| --- | --- |
| Physical apparatus | Single-piece PETG reservoir, integrated outlet, flexible silicone tube and externally mounted 3D-printed servo pinch valve |
| Instrumentation | ELEGOO UNO R3, HC-SR04 ultrasonic sensor, USB logging and independently collected outlet volume |
| Computational model | Reservoir continuity, calibrated discharge relationship, measurement filtering and uncertainty analysis in Python |
| Digital twin | Dimensionally accurate CAD geometry displayed in Three.js, synchronized with observations and predicted levels |

The governing water balance is

```text
dV/dt = Q_in - Q_controlled - Q_leak - Q_evaporation
```

For constant-area geometry, `V = A h`. The level sensor observes net storage change. Without independent knowledge or bounds on controlled discharge and other losses, an individual leak cannot be uniquely identified.

*Figure 1 in the author-supplied Word document: conceptual reservoir with ultrasonic sensor, inflow, controlled outlet, test loss path and evaporation. Figure 2: physical apparatus → measurements and ground truth → calibrated hydraulic model → detection algorithms, evaluated using independent trials.*

## Experimental approach

- Calibrate ultrasonic depth measurements against independent water-depth and volume observations. Quantify error, repeatability, drift and invalid echoes.
- Characterize ordinary discharge for selected hydraulic heads and commanded servo positions using timed collection.
- Introduce a controlled additional discharge during normal valve operations. Retain ground-truth loss rates.
- Compare a fixed threshold, CUSUM-type statistical detector and uncertainty-aware model residual on held-out trials.
- Report sensitivity, false-alarm rate, minimum detectable additional loss, detection latency and prediction error.

## Present status and preliminary specifications

The GitHub repository, initial Python hydraulic unit tests, preliminary FreeCAD model and design note DN-001 have been developed. No printed reservoir, calibrated sensing dataset or validated leak-detection results are yet available.

Proposed internal dimensions: 140 × 100 × 160 mm; proposed operating depth: 120 mm; nominal operating volume: 1.68 L. These require fabrication and dimensional verification.

## Scope and limitations

**Initial research scope.** The first apparatus is an open, gravity-drained storage reservoir operating under documented conditions. The intended deliverable is a reproducible relationship among additional loss rate, observation time, measurement uncertainty and detection performance. We will compare hydraulic-model-informed detection with simpler alarm approaches, including trials where available observations do not permit a reliable conclusion. Public geometry, firmware, analysis code, calibration datasets and protocols would support replication.

**Identifiability and external validity.** A single depth sensor measures net change in storage. If intended withdrawals and incidental losses are unknown, an additional leak is not uniquely observable. Ambient pressure generally cancels between an open tank and an atmospheric outlet, while temperature can influence ultrasound ranging and evaporation. This apparatus does not reproduce pressurized pipe transients, spatial demand patterns, utility SCADA environments or leak localization. Claims of municipal-network or industrial field performance would be premature.

**Potential follow-on research.** After validation, add independently measured flow or mass, vary reservoir geometry, or connect multiple printed tanks and pipes. Compare incremental sensor reliability per dollar. A later modular pipe network could investigate sensor placement and fault localization but requires new pressure/flow instrumentation and different hydraulic models.

**Prospective industry pathways.** The design and research dataset could support laboratory/teaching equipment. Later developments might serve noncritical industrial storage monitoring or software that evaluates existing sensor streams. Any real-site pilot must establish sensor ruggedness, environmental/electrical performance, maintainability, secure data handling, operational integration and the tradeoff between false alarms and avoided water losses. None of these are currently demonstrated commercial capabilities.

## Feedback requested from ENV E 320 professor

- Is the water-balance and uncertainty question sufficiently well defined?
- Which hydrological principles and measurement techniques would improve experimental validity?
- What is the appropriate benchmark detector and independent reference measurement?
- Is the apparatus size suitable for a defensible undergraduate research contribution?
- Which research output is most valuable: detection-limit curves, instrumentation-value comparisons or model transferability?
- Are there relevant publications, facilities or opportunities for research supervision?

## CAD appendix

The original six-page Word overview includes top, front, bottom and left orthographic views of the preliminary FreeCAD assembly on pages 5–6. Refer to the original document and the editable CAD files for graphical detail and verified dimensions.

Project: https://github.com/Codegeasspro/HydroSense
