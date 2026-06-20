"""
Professional Python Lab Challenge (Kata).
Implement an asynchronous orchestrator that fetches item details concurrently.
"""

import asyncio
from typing import Callable, Coroutine, Any


async def fetch_item_details(
    item_id: int, fetch_fn: Callable[[int], Coroutine[Any, Any, str]]
) -> list[str]:
    """
    Given a list of item IDs (from 1 up to item_id) and a coroutine function fetch_fn,
    execute all fetch coroutines concurrently using asyncio.gather.
    Returns:
        List of result strings.
    """
    tasks = [fetch_fn(i) for i in range(1, item_id + 1)]
    results = await asyncio.gather(*tasks)
    return list(results)
