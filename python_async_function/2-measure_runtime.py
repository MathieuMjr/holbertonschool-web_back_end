#!/usr/bin/env python3
"""
Docstring pour python_async_function.2-measure_runtime
"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Docstring pour measure_time

    :param n: number of loop
    :type n: int
    :param max_delay: maximum time async.sleep
    :type max_delay: int
    :return: time of execution
    :rtype: float
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    return (end - start)
