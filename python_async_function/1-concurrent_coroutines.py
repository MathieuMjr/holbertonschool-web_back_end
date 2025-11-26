#!/usr/bin/env python3
"""
Docstring pour python_async_function.1-concurrent_coroutines
Contains a function that perform n time wait_random
with a specific maximum delay
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Docstring pour wait_n

    :param n: Number of time to call wait_random
    :type n: int
    :param max_delay: Maximum value of asyncio.sleep
    :type max_delay: int
    :return: The list of delays
    :rtype: List[float]
    """
    new_list = []
    for i in range(0, n):
        new_list.append(await wait_random(max_delay))
    return new_list
