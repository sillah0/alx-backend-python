#!/usr/bin/env python3
"""9-element_length.py"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a function that """
    return [(i, len(i)) for i in lst]
