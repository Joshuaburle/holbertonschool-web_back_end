#!/usr/bin/env python3
"""This module defines an asynchronous generator that yields random numbers."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random numbers asynchronously with a 1-second delay."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
