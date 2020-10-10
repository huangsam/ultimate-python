import time
from concurrent import futures
from datetime import datetime

# Module-level constants
_MULTIPLY_DELAY = 0.001


def multiply_by_two(item):
    """This multiplication has a small delay."""
    time.sleep(_MULTIPLY_DELAY)
    return item * 2


def run_workers(work, data):
    results = set()

    # We can use a with statement to ensure threads are cleaned up promptly
    with futures.ThreadPoolExecutor() as executor:
        future_iterable = (executor.submit(work, item) for item in data)

        # Note that future outcomes are returned out of order
        for future in futures.as_completed(future_iterable):
            results.add(future.result())

    return results


def main():
    original_data = {1, 2, 3, 4}
    expected_data = {(item * 2) for item in original_data}

    # Let's get the data using the simple approach
    simple_start = datetime.now()
    simple_data = {multiply_by_two(item) for item in original_data}
    simple_duration = datetime.now() - simple_start

    # The simple approach has the expected data
    assert simple_data == expected_data

    # Let's get the data using the threaded approach
    thread_start = datetime.now()
    thread_data = run_workers(multiply_by_two, original_data)
    thread_duration = datetime.now() - thread_start

    # The threaded approach has the expected data
    assert thread_data == expected_data

    # But the threaded approach is faster than the simple approach because
    # threads are a form of cooperative multitasking where a blocking call
    # like time.sleep forces the current thread to yield its control over
    # to a waiting thread to start running. That means the threaded approach
    # can run multiple blocking operations at a time whereas the simple
    # approach can only run one blocking operation at a time
    assert thread_duration < simple_duration


if __name__ == '__main__':
    main()
