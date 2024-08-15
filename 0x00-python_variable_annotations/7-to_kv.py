#!/usr/bin/env python3
"""7-to_kv.py"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple
    """
     return (k, v ** 2)
