#!/usr/bin/env python3
"""Module that provides a multiplier factory function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""

    def multiply(x: float) -> float:
        """Multiplies x by the captured multiplier."""
        return x * multiplier

    return multiply
