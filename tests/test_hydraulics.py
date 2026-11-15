import pytest
from hydrosense.hydraulics import (
    CUSUMDetector,
    assess_volume_residual,
    depth_from_echo_m,
    predicted_volume_m3,
    storage_m3,
    volume_uncertainty_m3,
)

def test_design_volume():
    assert storage_m3(0.14, 0.10, 0.12) == pytest.approx(0.00168)

def test_depth_calibration():
    assert depth_from_echo_m(0.20, 0.08) == pytest.approx(0.12)

def test_negative_dimensions_rejected():
    with pytest.raises(ValueError):
        storage_m3(0.14, -0.10, 0.12)


def test_predicted_volume_without_abnormal_loss():
    assert predicted_volume_m3(0.00168, 0.0, 1e-6, 60.0) == pytest.approx(0.00162)


def test_uncertainty_propagates_level_and_flow_terms():
    uncertainty = volume_uncertainty_m3(
        surface_area_m2=0.014,
        level_standard_uncertainty_m=0.001,
        initial_volume_standard_uncertainty_m3=1e-6,
        inflow_standard_uncertainty_m3_s=0.0,
        outflow_standard_uncertainty_m3_s=1e-7,
        elapsed_s=60.0,
    )
    assert uncertainty == pytest.approx((0.000014**2 + 0.000001**2 + 0.000006**2) ** 0.5)


def test_negative_residual_alerts_only_beyond_uncertainty_threshold():
    normal = assess_volume_residual(0.00167, 0.00168, 0.00001)
    alert = assess_volume_residual(0.00164, 0.00168, 0.00001)
    assert normal.status == "normal"
    assert alert.status == "alert"
    assert alert.normalized_residual == pytest.approx(-4.0)


def test_cusum_detects_persistent_negative_shift():
    detector = CUSUMDetector(reference_value=0.01, decision_interval=0.05)
    assert detector.update(-0.02) == "normal"
    assert detector.update(-0.02) == "normal"
    assert detector.update(-0.02) == "normal"
    assert detector.update(-0.02) == "normal"
    assert detector.update(-0.02) == "low_alert"
