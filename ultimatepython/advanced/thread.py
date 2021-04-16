"""
Threaded programming is used by developers to improve the performance of
an application. This module shows a simple multiplication operation with
some delay can be parallelized using `ThreadPoolExecutor`. A good grasp of
operating systems and CPUs is recommended before reading the code below.
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Module-level constants
_MULTIPLY_DELAY = 0.01


def multiply_by_two(item):
    """This multiplication has a small delay."""
    time.sleep(_MULTIPLY_DELAY)
    return item * 2


def run_thread_workers(work, data):
    """Run thread workers that invoke work on each data element."""
    results = set()

    # We can use a with statement to ensure workers are cleaned up promptly
    with ThreadPoolExecutor() as executor:
        # Note that results are returned out of order
        work_queue = (executor.submit(work, item) for item in data)
        for future in as_completed(work_queue):
            results.add(future.result())

    return results


def main():
    original_data = {num for num in range(5)}
    expected_data = {(item * 2) for item in original_data}

    # Let's get the data using the simple approach
    simple_start = datetime.now()
    simple_data = {multiply_by_two(item) for item in original_data}
    simple_duration = datetime.now() - simple_start

    # The simple approach has the expected data
    assert simple_data == expected_data

    # Let's get the data using the threaded approach
    thread_start = datetime.now()
    thread_data = run_thread_workers(multiply_by_two, original_data)
    thread_duration = datetime.now() - thread_start

    # The threaded approach has the expected data
    assert thread_data == expected_data

    # The threaded approach is faster than the simple approach in this case
    # because a blocking I/O call like time.sleep forces the current thread
    # to yield its control over to a waiting thread to start running. That
    # means the threaded approach can run blocking operations in parallel.
    # The cost of creating threads is somewhat cheap which means we often
    # create more than one thread to speed up I/O-heavy workloads
    assert thread_duration < simple_duration

    # However, Python threads are not suitable for CPU-heavy tasks in the
    # CPython interpreter due to the GIL. To address this, we typically
    # resort to forking processes or running C externally. Both approaches
    # have their own pros and cons


if __name__ == "__main__":
    main()
