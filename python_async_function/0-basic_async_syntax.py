#!/usr/bin/env python3
"""
Docstring pour python_async_function.0-basic_async_syntax
Contains a function that wait randomly beetween 0 and
a max_delay value number of seconds
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    function that wait randomly beetween 0 and
    a max_delay value number of seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
