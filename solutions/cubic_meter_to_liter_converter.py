#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to convert cubic meters to liters.

Module contents:
    - cubic_meter_to_liter: Converts a volume in cubic meters to liters.

Created on 2025-01-10
Author: Cyne Jarvis J. Zarceno
"""


def cubic_meter_to_liter(cubic_meters: float) -> float:
    """
    Convert a volume from cubic meters to liters.

    Args:
        cubic_meters (float): Volume in cubic meters. Must be non-negative.

    Returns:
        float: Volume in liters, rounded to 2 decimal places.

    Raises:
        TypeError: If cubic_meters is not a number (int or float).
        ValueError: If cubic_meters is negative.

    Examples:
        >>> cubic_meter_to_liter(1.0)
        1000.00
        >>> cubic_meter_to_liter(0.001)
        1.00
        >>> cubic_meter_to_liter(5.0)
        5000.00
    """
    if not isinstance(cubic_meters, (int, float)):
        raise TypeError("Input must be a number")

    if cubic_meters < 0:
        raise ValueError("Volume cannot be negative")

    # Convert cubic meters to liters
    liters = cubic_meters * 1000
    return round(liters, 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
