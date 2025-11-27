#!/usr/bin/env python
"""
Docstring pour python_async_comprehension.0-async_generator
"""
from typing import AsyncGenerator, Any
from random import randint
import asyncio


async def async_generator() -> AsyncGenerator[Any, None]:
    """
    Docstring pour async_generator

    :return: Description
    :rtype: AsyncGenerator[Any, None]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield randint(0, 10)
