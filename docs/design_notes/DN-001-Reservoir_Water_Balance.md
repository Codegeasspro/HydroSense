# Design Note 001: Reservoir Water Balance

_Transcription of “DN-001-Reservoir Water Balance.docx” supplied by the project author. Original wording retained, with embedded Word equations transcribed into LaTeX. This is a Markdown companion, not the original Word binary._

## Question

Why does decreasing water level not prove leakage?

- A decrease in water level indicates a reduction in stored volume, assuming reservoir geometry remains unchanged. It does not independently establish the mechanism responsible.
- Potential causes include controlled discharge, unintended leakage, evaporation, and measurement error.

## Known Information

- The preliminary reservoir geometry is 140 × 100 × 160 mm internally. Its proposed maximum operating water depth is 120 mm, corresponding to a storage capacity of 1.68L.
- The system will use an HC-SR04 ultrasonic sensor and a servo-operated outlet valve.
- These dimensions and components are design specifications, not experimentally validated measurements.

## Engineering Analysis

Water Balance Equation for the reservoir:

$$
\frac{dV}{dt}=Q_{in}-Q_{out}-Q_{leak}-Q_{evaporation}
$$

Rectangular Reservoir:

$$
V=A\times h
$$

Therefore, measured water-level changes represent the combined effects of all sources and sinks.

## Uncertainties

- The principal uncertainties are sensor measurement error, actual valve discharge, evaporation, reservoir deformation, and unintended water loss.
- Ambient temperature may affect sensor performance and evaporation. Reservoir material may influence deformation and leakage through printed surfaces.

## Next Steps

- First, measure water-level changes with the outlet closed. Then characterize controlled discharge at known valve positions using independently collected water volumes.
- Compare observed storage changes with predicted changes to identify unexplained losses.
