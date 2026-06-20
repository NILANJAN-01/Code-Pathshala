"""
Garbage Collection and Reference Cycles Module.
Demonstrates how Python detects and cleans reference cycles (circular references).
"""

import gc
from typing import Any


class Node:
    """A node that can link to other nodes, useful for creating reference cycles."""

    def __init__(self, name: str):
        self.name = name
        self.link: Any = None


def create_and_collect_cycle() -> int:
    """
    Creates a circular reference between two Node objects, deletes external pointers,
    and calls the garbage collector to sweep the reference cycle.
    Returns:
        The number of unreachable objects collected.
    """
    # 1. Disable GC to ensure we control the timing of the cleanup
    gc.disable()

    # 2. Create the circular references
    node_a = Node("Node A")
    node_b = Node("Node B")
    node_a.link = node_b
    node_b.link = node_a

    # 3. Orphan the cycle (delete the reference pointers from our local scope stack frame)
    del node_a
    del node_b

    # 4. Trigger GC collection and measure reclaimed objects
    # This will locate the cyclic references and clean them up
    unreachable_count = gc.collect()

    # Re-enable GC
    gc.enable()

    return unreachable_count
