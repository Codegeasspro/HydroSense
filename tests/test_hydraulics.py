import pytest
from hydrosense.hydraulics import storage_m3, depth_from_echo_m

def test_design_volume():
    assert storage_m3(0.14, 0.10, 0.12) == pytest.approx(0.00168)

def test_depth_calibration():
    assert depth_from_echo_m(0.20, 0.08) == pytest.approx(0.12)

def test_negative_dimensions_rejected():
    with pytest.raises(ValueError):
        storage_m3(0.14, -0.10, 0.12)
