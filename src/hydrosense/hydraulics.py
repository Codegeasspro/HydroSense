"""Unit-consistent storage calculations and transparent anomaly benchmarks.

These functions are research utilities. They do not establish a physical leak,
water safety, or actuator command without calibrated inputs and ground truth.
"""

from dataclasses import dataclass
from math import isclose, sqrt


@dataclass(frozen=True)
class ResidualAssessment:
    """Result of comparing a measured tank volume with a predicted volume."""

    residual_m3: float
    standard_uncertainty_m3: float
    normalized_residual: float
    status: str

def storage_m3(length_m: float, width_m: float, depth_m: float) -> float:
    """Compute water storage in m^3 for a uniform rectangular section."""
    if min(length_m, width_m, depth_m) < 0:
        raise ValueError("Geometry and depth must not be negative")
    return length_m * width_m * depth_m

def depth_from_echo_m(sensor_to_bottom_m: float, distance_m: float) -> float:
    """Convert calibrated sensor-to-water echo distance into water depth."""
    if sensor_to_bottom_m <= 0 or distance_m < 0:
        raise ValueError("Invalid measured distance or datum")
    depth = sensor_to_bottom_m - distance_m
    if depth < 0:
        raise ValueError("Water echo is below calibrated tank bottom")
    return depth


def predicted_volume_m3(
    initial_volume_m3: float,
    inflow_m3_s: float,
    expected_outflow_m3_s: float,
    elapsed_s: float,
) -> float:
    """Predict storage after a continuity-model time step without abnormal loss."""
    if initial_volume_m3 < 0 or elapsed_s < 0:
        raise ValueError("Initial volume and elapsed time must not be negative")
    return initial_volume_m3 + (inflow_m3_s - expected_outflow_m3_s) * elapsed_s


def volume_uncertainty_m3(
    surface_area_m2: float,
    level_standard_uncertainty_m: float,
    initial_volume_standard_uncertainty_m3: float,
    inflow_standard_uncertainty_m3_s: float,
    outflow_standard_uncertainty_m3_s: float,
    elapsed_s: float,
) -> float:
    """Propagate independent one-standard-deviation terms for a time step.

    The function intentionally uses a simple independent-error model. Correlated
    errors, geometry uncertainty, and timing uncertainty must be added explicitly
    before using results for an experiment.
    """
    values = (
        surface_area_m2,
        level_standard_uncertainty_m,
        initial_volume_standard_uncertainty_m3,
        inflow_standard_uncertainty_m3_s,
        outflow_standard_uncertainty_m3_s,
        elapsed_s,
    )
    if any(value < 0 for value in values):
        raise ValueError("Uncertainty terms, surface area, and elapsed time must not be negative")
    measured_volume_uncertainty = surface_area_m2 * level_standard_uncertainty_m
    predicted_volume_uncertainty = sqrt(
        initial_volume_standard_uncertainty_m3**2
        + (elapsed_s * inflow_standard_uncertainty_m3_s) ** 2
        + (elapsed_s * outflow_standard_uncertainty_m3_s) ** 2
    )
    return sqrt(measured_volume_uncertainty**2 + predicted_volume_uncertainty**2)


def assess_volume_residual(
    measured_volume_m3: float,
    predicted_volume_m3_value: float,
    standard_uncertainty_m3: float,
    alert_sigma: float = 3.0,
) -> ResidualAssessment:
    """Classify a residual as normal, alert, or indeterminate.

    A negative residual means less measured water than predicted. This is an
    unexplained-loss candidate, not proof of a leak location or root cause.
    """
    if measured_volume_m3 < 0 or predicted_volume_m3_value < 0:
        raise ValueError("Volumes must not be negative")
    if standard_uncertainty_m3 <= 0 or alert_sigma <= 0:
        raise ValueError("Uncertainty and alert sigma must be positive")
    residual = measured_volume_m3 - predicted_volume_m3_value
    normalized = residual / standard_uncertainty_m3
    status = "alert" if normalized <= -alert_sigma else "normal"
    return ResidualAssessment(residual, standard_uncertainty_m3, normalized, status)


class CUSUMDetector:
    """Two-sided cumulative-sum benchmark for residual time series.

    This implementation is deliberately small and transparent. Detector settings
    must be fitted on development trials and frozen before held-out evaluation.
    """

    def __init__(self, reference_value: float, decision_interval: float) -> None:
        if reference_value < 0 or decision_interval <= 0:
            raise ValueError("Reference value must be non-negative and decision interval positive")
        self.reference_value = reference_value
        self.decision_interval = decision_interval
        self.positive_sum = 0.0
        self.negative_sum = 0.0

    def update(self, observation: float, target: float = 0.0) -> str:
        """Update cumulative sums and return normal, high_alert, or low_alert."""
        deviation = observation - target
        self.positive_sum = max(0.0, self.positive_sum + deviation - self.reference_value)
        self.negative_sum = min(0.0, self.negative_sum + deviation + self.reference_value)
        if self.positive_sum >= self.decision_interval or isclose(
            self.positive_sum, self.decision_interval, abs_tol=1e-12
        ):
            return "high_alert"
        if self.negative_sum <= -self.decision_interval or isclose(
            self.negative_sum, -self.decision_interval, abs_tol=1e-12
        ):
            return "low_alert"
        return "normal"
