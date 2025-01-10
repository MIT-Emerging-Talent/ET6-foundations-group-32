#!/usr/bin/env python3
"""
This module contains a function to calculate the sum of all even numbers
from 1 to a given number.

Function:
 - sum_of_evens: Returns the sum of all even numbers within the given range.

@author Thandar Htwer (Marshar)
Created on Jan 8, 2025
"""


def sum_of_evens(n: int) -> int:
    """
    Calculate the sum of all even numbers from 1 to n.

    Parameters:
        n (int): The upper limit of the range (inclusive).

    Returns:
        int: The sum of all even numbers from 1 to n.

    Raises:
        ValueError: If the input is not a non-negative integer.

    Examples:
        >>> sum_of_evens(10)
        30
        >>> sum_of_evens(5)
        6
        >>> sum_of_evens(1)
        0
    """
   # Defensive assertions
    assert isinstance(n, int), "Input must be an integer."
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Calculate sum of evens
    return sum(num for num in range(1, n + 1) if num % 2 == 0)
