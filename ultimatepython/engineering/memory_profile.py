"""
While CPU profiling (`cProfile`) identifies execution bottlenecks, memory profiling
diagnoses RAM consumption, high allocations, and memory leaks.

Python's built-in `tracemalloc` module tracks memory blocks allocated by Python.
By capturing snapshots before and after operations, developers can compute allocation
deltas line by line to pinpoint which statements consume the most heap space.
"""

import tracemalloc


def allocate_payload(count: int) -> list[str]:
    """Allocate a collection of formatted string records."""
    return [f"record_payload_{i}" for i in range(count)]


def main() -> None:
    # 1. Start tracking memory allocations
    tracemalloc.start()
    assert tracemalloc.is_tracing() is True

    # 2. Take a baseline snapshot before creating objects
    snapshot_before = tracemalloc.take_snapshot()

    # 3. Perform an operation that allocates memory on the heap
    payload = allocate_payload(5_000)

    # 4. Take a second snapshot to evaluate allocation delta
    snapshot_after = tracemalloc.take_snapshot()

    # 5. Measure current vs peak memory during the tracing session
    current_bytes, peak_bytes = tracemalloc.get_traced_memory()
    assert current_bytes > 0
    assert peak_bytes >= current_bytes

    # 6. Compare snapshots grouped by source line number to find top consumers
    stats = snapshot_after.compare_to(snapshot_before, "lineno")
    assert len(stats) > 0

    # The top allocation difference should be our list comprehension in allocate_payload
    top_stat = stats[0]
    assert top_stat.size_diff > 0
    assert top_stat.count_diff > 0
    assert "memory_profile.py" in top_stat.traceback.format()[0]

    # Clean up memory reference and stop tracing
    del payload
    tracemalloc.stop()
    assert tracemalloc.is_tracing() is False


if __name__ == "__main__":
    main()
