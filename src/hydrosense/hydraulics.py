"""Simple, unit-consistent storage calculations for a rectangular tank."""

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
