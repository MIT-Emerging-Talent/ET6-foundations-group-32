#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function that categorizes members into specific criteria
on age and skill level

Module contents:
    - categorize_member: a function that categorizes members into specific criteria
    on age and skill level

Created on: 2025-01-07
@author: KarimMakki
"""


def categorize_member(age: int, handicap: int) -> str:
    """Categorizes an individual into a membership program based on their age and handicap.

    Parameters:
        age (int): The individual's age. Must be non-negative and at least 10
        handicap (int): The individual's skill level. Must be between 0 and 10

    Returns:
        str: The membership category ("Junior", "High Skill Junior, "Intermediate",
        "Low Skill Intermediate", "High Skill Intermediate", "Senior", "Low Skill Senior")

    Raises:
        AssertionError:
        -  If age is not an integer
        -  If handicap is not an integer
        ValueError:
        -  If the age is negative integer
        -  If the age is less than 10
        -  If the handicap is out of range (0 to 10)

    Examples:
        >>> categorize_member(17, 2)
        'Junior'
        >>> categorize_member(14, 7)
        'High Skill Junior'
        >>> categorize_member(25, 5)
        'Intermediate'
        >>> categorize_member(30, 2)
        'Low Skill Intermediate'
    """

    # Validate inputs type
    assert isinstance(age, int), "Age must be an integer"
    assert isinstance(handicap, int), "Handicap must be an integer"

    # Value range validation
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 10:
        raise ValueError("Age cannot be less than 10")
    if not 0 <= handicap <= 10:
        raise ValueError("Handicap must be between 0 and 10")

    # Junior members age less than 18
    if age < 18:
        if 0 <= handicap <= 3:
            return "Junior"
        # "High Skill Junior" for handicap above 3
        else:
            return "High Skill Junior"

    # Intermediate members age range 18-54
    if age >= 18 and age < 55:
        if 4 <= handicap <= 7:
            return "Intermediate"
        # "Low Skill Intermediate" for handicap less than 4
        elif handicap < 4:
            return "Low Skill Intermediate"
        # "High Skill Intermediate" for handicap above 7
        else:
            return "High Skill Intermediate"

    # Senior members age above 55
    if age >= 55:
        if 8 <= handicap <= 10:
            return "Senior"
        # "Low Skill Senior" for handicap less than 8
        elif handicap < 8:
            return "Low Skill Senior"
