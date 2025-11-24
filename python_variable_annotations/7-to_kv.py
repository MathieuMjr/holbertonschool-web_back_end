#!/usr/bin/env python3
"""
This module contains a function
that return a tuple of a string
and a float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a string and
    a the square of a number in a tuple
    """
    return (k, v**2)
