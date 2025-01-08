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
        age (int): The individual's age. Must be non-negative.
        handicap (int): The individual's skill level. Must be between 0 and 10.

    Returns:
        str: The membership category ("Junior", "Senior", "Intermediate", or "Open")

    Raises:
        AssertionError:
        -  If age is not an integer
        -  If handicap is not an integer
        ValueError:
        -  If the age is negative integer
        -  If the handicap is out of range (0 to 10)

    Examples:
        >>> categorize_member(17, 2)
        'Junior'
        >>> categorize_member(55, 8)
        'Senior'
        >>> categorize_member(25, 5)
        'Intermediate'
        >>> categorize_member(45, 9)
        'Open'
    """

    # Validate inputs type
    assert isinstance(age, int), "Age must be an integer"
    assert isinstance(handicap, int), "Handicap must be an integer"

    # Value range validation
    if age < 0:
        raise ValueError("Age cannot be negative")
    if not 0 <= handicap <= 10:
        raise ValueError("Handicap must be between 0 and 10")

    # Age is less than 18 AND handicap in range 0-3
    if age < 18 and 0 <= handicap <= 3:
        return "Junior"
    # Age is 55 or older AND handicap in range 8-10
    elif age >= 55 and 8 <= handicap <= 10:
        return "Senior"
    # Age is 18 or older AND handicap in range 4-7
    elif age >= 18 and 4 <= handicap <= 7:
        return "Intermediate"
    # Any other case
    else:
        return "Open"
