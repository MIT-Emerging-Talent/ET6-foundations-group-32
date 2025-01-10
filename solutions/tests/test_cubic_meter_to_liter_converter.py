#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for cubic_meter_to_liter function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: Valid positive float and integer inputs
    - Edge cases: Very small and very large volumes
    - Defensive cases: Invalid input types and negative values

Created on 2025-01-10
Author: Cyne Jarvis J. Zarceno
"""

import sys
import os
import unittest
from solutions.cubic_meter_to_liter_converter import cubic_meter_to_liter

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCubicMeterToLiterConverter(unittest.TestCase):
    """Test cases for cubic_meter_to_liter function."""

    def test_one_cubic_meter(self):
        """Test conversion of 1.0 cubic meter."""
        self.assertAlmostEqual(cubic_meter_to_liter(1.0), 1000.00, places=2)

    def test_half_cubic_meter(self):
        """Test conversion of 0.5 cubic meters."""
        self.assertAlmostEqual(cubic_meter_to_liter(0.5), 500.00, places=2)

    def test_small_volume(self):
        """Test conversion of small volume (0.001 cubic meters)."""
        self.assertAlmostEqual(cubic_meter_to_liter(0.001), 1.00, places=2)

    def test_large_volume(self):
        """Test conversion of large volume (1000.0 cubic meters)."""
        self.assertAlmostEqual(cubic_meter_to_liter(1000.0), 1000000.00, places=2)

    def test_zero_volume(self):
        """Test conversion of zero cubic meters."""
        self.assertAlmostEqual(cubic_meter_to_liter(0), 0.00, places=2)

    def test_integer_input(self):
        """Test conversion with integer input."""
        self.assertAlmostEqual(cubic_meter_to_liter(5), 5000.00, places=2)

    def test_raises_type_error_with_string(self):
        """Test TypeError raised with string input."""
        with self.assertRaises(TypeError):
            cubic_meter_to_liter("1.0")

    def test_raises_type_error_with_list(self):
        """Test TypeError raised with list input."""
        with self.assertRaises(TypeError):
            cubic_meter_to_liter([1.0])

    def test_raises_value_error_with_negative(self):
        """Test ValueError raised with negative input."""
        with self.assertRaises(ValueError):
            cubic_meter_to_liter(-1.0)


if __name__ == "__main__":
    unittest.main()
