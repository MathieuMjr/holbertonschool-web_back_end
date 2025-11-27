#!/usr/bin/env python
"""
Docstring pour python_async_comprehension.0-async_generator
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    Docstring pour async_generator

    :return: Description
    :rtype: AsyncGenerator[Any, None]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
