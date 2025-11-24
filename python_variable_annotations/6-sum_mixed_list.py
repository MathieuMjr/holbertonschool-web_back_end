#!/usr/bin/env python3
"""
This module contains a function
that make the sum of floats in
a list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that makes the sum
    of floats in a list
    """
    res: float = 0
    for n in mxd_lst:
        res += n
    return res
