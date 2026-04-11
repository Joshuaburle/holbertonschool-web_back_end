#!/usr/bin/env python3
"""Module that defines async_comprehension coroutine."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator using async comprehension."""
    return [value async for value in async_generator()]
