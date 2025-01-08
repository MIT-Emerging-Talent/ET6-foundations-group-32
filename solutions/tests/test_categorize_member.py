#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for categorize_member function.
Contains correct tests to help identify bugs in the implementation

Test categories:
    - Standard cases: Standard membership categorization tests cases (Junior, Intermediate,
    Senior, Open)
    - Edge cases: Boundary conditions for age and handicap values
    - Defensive cases: Input validation and error handling tests

Created on 2025-01-07
@author: KarimMakki
"""

import unittest

from ..categorize_member import categorize_member


class TestCategorizeMember(unittest.TestCase):
    """Tests for categorize member function"""

    # Standard tests cases
    def test_junior_member(self):
        """it should evaluate (16, 2) to Junior"""
        actual = categorize_member(16, 2)
        expected = "Junior"
        self.assertEqual(actual, expected)

    def test_intermediate_member(self):
        """it should evaluate (22, 5) to Intermediate"""
        actual = categorize_member(22, 5)
        expected = "Intermediate"
        self.assertEqual(actual, expected)

    def test_senior_member(self):
        """it should evaluate (60, 9) to Senior"""
        actual = categorize_member(60, 9)
        excepted = "Senior"
        self.assertEqual(actual, excepted)

    def test_open_member_1(self):
        """it should evaluate (15, 7) to Open"""
        actual = categorize_member(15, 7)
        expected = "Open"
        self.assertEqual(actual, expected)

    def test_open_member_2(self):
        """it should evaluate (40, 8) to Open"""
        actual = categorize_member(40, 8)
        expected = "Open"
        self.assertEqual(actual, expected)

    def test_open_member_3(self):
        """it should evaluate (14, 7) to Open"""
        actual = categorize_member(55, 3)
        expected = "Open"
        self.assertEqual(actual, expected)

    # Edge cases
    def test_minimum_values(self):
        """it should handle minimum possible values"""
        self.assertEqual(categorize_member(0, 0), "Junior")

    def test_age_boundary_junior(self):
        """it should evaluate (17, 2) as Junior at age boundary"""
        self.assertEqual(categorize_member(17, 2), "Junior")

    def test_age_boundary_intermediate(self):
        """it should evaluate (18, 5) as Intermediate at minimum age"""
        self.assertEqual(categorize_member(18, 5), "Intermediate")

    def test_age_boundary_senior(self):
        """it should evaluate (55, 9) as Senior at minimum senior age"""
        self.assertEqual(categorize_member(55, 9), "Senior")

    def test_minimum_handicap_junior(self):
        """it should evaluate cases at Junior minimum handicap"""
        self.assertEqual(categorize_member(16, 0), "Junior")

    def test_maximum_handicap_junior(self):
        """it should evaluate cases at Junior maximum handicap"""
        self.assertEqual(categorize_member(16, 3), "Junior")

    def test_minimum_handicap_intermediate(self):
        """it should evaluate cases at Intermediate minimum handicap"""
        self.assertEqual(categorize_member(25, 4), "Intermediate")

    def test_maximum_handicap_intermediate(self):
        """it should evaluate cases at Intermediate maximum handicap"""
        self.assertEqual(categorize_member(25, 7), "Intermediate")

    def test_minimum_handicap_senior(self):
        """it should evaluate cases at Senior minimum handicap"""
        self.assertEqual(categorize_member(60, 8), "Senior")

    def test_maximum_handicap_senior(self):
        """it should evaluate cases at Senior maximum handicap"""
        self.assertEqual(categorize_member(60, 10), "Senior")

    # Defensive cases
    def test_invalid_age_type(self):
        """it should raise AssertionError for non-integer age"""
        with self.assertRaises(AssertionError):
            categorize_member("55", 7)

    def test_invalid_handicap_type(self):
        """it should raise AssertionError for non-integer handicap"""
        with self.assertRaises(AssertionError):
            categorize_member(55, "7")

    def test_none_age_value(self):
        """it should raise AssertionError for None age value"""
        with self.assertRaises(AssertionError):
            categorize_member(None, 7)

    def test_negative_age(self):
        """it should raise ValueError for negative age"""
        with self.assertRaises(ValueError):
            categorize_member(-1, 5)

    def test_invalid_handicap_range(self):
        """it should raise ValueError for out-of-range handicap"""
        with self.assertRaises(ValueError):
            categorize_member(55, -1)
