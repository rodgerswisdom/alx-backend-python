#!/usr/bin/env python3

"""
0-basic_async_synatax.py - a module demonstrating the used of async and await.

This module provides an asynchronous coroutine that waits for a random delay between 0 and max_delay seconds and returns the delay.
"""

import asyncio
import random

async def wait_random(max_delay: float = 10.0) -> float:
	"""
	wait_random(max_delay: float = 10.0) -> float

    Wait for a random delay between 0 and max_delay seconds and return the delay.

    Args:
        max_delay (float, optional): The maximum delay to wait. Defaults to 10.0.

    Returns:
        float: The random delay waited.
	"""
	delay = random.uniform(1, max_delay)
	await asyncio.sleep(delay)
	return delay

