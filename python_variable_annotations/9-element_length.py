#!/usr/bin/env python3
"""
This module contains a function that returns
tuples with iterable and iterable lenght
from a sequence
"""
from typing import Sequence, Any, Iterable, Tuple, List


def element_length(lst: Sequence[Iterable[Any]]) -> List[
    Tuple[Iterable[Any]], int
        ]:
    """
    This function returns tuples of an Iterable
    and it's length from a sequence
    """
    return [(i, len(i)) for i in lst]
