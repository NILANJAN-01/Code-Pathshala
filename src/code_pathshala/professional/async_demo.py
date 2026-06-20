"""
Asynchronous Programming Module.
Demonstrates non-blocking cooperative multitasking using async/await and asyncio.
"""

import asyncio
import time


async def fetch_task(task_id: int, delay: float) -> str:
    """Simulates fetching some data concurrently with a sleep delay."""
    await asyncio.sleep(delay)
    return f"Task {task_id} completed (delay: {delay}s)"


async def run_concurrent_fetches() -> tuple[list[str], float]:
    """
    Executes multiple fetch operations concurrently using asyncio.gather.
    Returns the results and the total elapsed time.
    """
    start_time = time.perf_counter()

    # Run three tasks concurrently (total sleep sum is 2.5s, but concurrent duration should be max delay = 1.0s!)
    results = await asyncio.gather(
        fetch_task(1, 0.5),
        fetch_task(2, 1.0),
        fetch_task(3, 0.2),
    )

    end_time = time.perf_counter()
    elapsed = end_time - start_time
    return list(results), elapsed
