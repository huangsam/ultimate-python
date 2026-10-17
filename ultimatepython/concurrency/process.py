"""
Process-based parallelism via multiprocessing and concurrent.futures.

While threads share memory and are constrained by CPython's Global Interpreter
Lock (GIL) for CPU-bound tasks, multiprocessing spawns independent operating
system processes. Each process has its own memory space and Python interpreter,
allowing CPU-intensive work to execute in parallel across multiple CPU cores.

Key patterns demonstrated:
- `ProcessPoolExecutor`: High-level interface for managing worker processes
- `os.getpid()`: Demonstrating execution across distinct process IDs
- `executor.map()`: Batch mapping inputs across worker processes
- `executor.submit()`: Fine-grained task submission with `Future` objects
- Exception propagation across process boundaries
"""

import os
from concurrent.futures import ProcessPoolExecutor


def compute_square(n: int) -> int:
    """CPU-bound task to square a number."""
    return n * n


def get_worker_pid(_: int) -> int:
    """Return the operating system process ID of the worker."""
    return os.getpid()


def failing_task(n: int) -> int:
    """Task that raises an exception to demonstrate inter-process error propagation."""
    if n < 0:
        raise ValueError("Input must be non-negative")
    return n


def main() -> None:
    main_pid = os.getpid()

    # 1. Direct execution establishes baseline behavior in the main process
    assert compute_square(3) == 9
    assert get_worker_pid(0) == main_pid
    assert failing_task(1) == 1
    direct_fail = False
    try:
        failing_task(-1)
    except ValueError:
        direct_fail = True
    assert direct_fail is True

    # 2. Using ProcessPoolExecutor with a controlled pool size
    with ProcessPoolExecutor(max_workers=2) as executor:
        # 3. executor.map processes inputs in parallel across worker processes
        numbers = [1, 2, 3, 4, 5]
        squares = list(executor.map(compute_square, numbers))
        assert squares == [1, 4, 9, 16, 25]

        # 3. Prove execution occurs in separate process IDs
        worker_pids = set(executor.map(get_worker_pid, range(4)))
        # Worker processes have their own PIDs, distinct from the main process
        assert main_pid not in worker_pids
        assert len(worker_pids) > 0

        # 4. executor.submit for individual asynchronous tasks
        future = executor.submit(compute_square, 12)
        assert future.result() == 144

        # 5. Exceptions raised in child processes propagate to future.result()
        failing_future = executor.submit(failing_task, -5)
        task_failed = False
        try:
            failing_future.result()
        except ValueError as e:
            task_failed = True
            assert str(e) == "Input must be non-negative"
        assert task_failed is True


if __name__ == "__main__":
    main()
