#!/usr/bin/env python3
"""Module that measures the runtime of four async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and return runtime."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.time()
    return end - start
