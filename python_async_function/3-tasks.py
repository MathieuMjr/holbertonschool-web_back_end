#!/usr/bin/env python3
"""
Docstring pour python_async_function.3-tasks
"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[Any]:
    """
    Docstring pour task_wait_random
    Create a task from async function

    :param max_delay: Max delay to pass tu the async function
    :type max_delay: int
    :return: async Task
    :rtype: Task[Any]
    """
    return asyncio.create_task(wait_random(max_delay))
