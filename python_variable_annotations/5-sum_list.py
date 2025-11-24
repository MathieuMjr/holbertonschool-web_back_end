#!/usr/bin/env python3
from typing import List
"""
This module contains a function
that make the sum of floats in
a list
"""


def sum_list(list: List[float]) -> float:
    """
    Function that makes the sum
    of floats in a list
    """
    res: float = 0
    for n in list:
        res += n
    return res
