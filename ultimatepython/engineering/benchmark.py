"""
As programs increase in size, they have the risk of getting slow as new
features are added and extra layers of complexity to the main features.
Benchmarking is an approach that helps developers use profiling metrics
and their code intuition to optimize programs further. This module uses
cProfile to compare the performance of two functions with each other,
showcasing the impact of caching/memoization with `functools.cache`.
"""

import cProfile
import io
import pstats
from functools import cache


def fib_naive(n: int) -> int:
    """Calculate Fibonacci number recursively without caching.

    This has O(2^N) time complexity due to redundant calculations.
    """
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


@cache
def fib_cached(n: int) -> int:
    """Calculate Fibonacci number recursively with caching.

    This has O(N) time complexity as each value is computed only once.
    """
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


def main() -> None:
    # Create a profile instance
    profile = cProfile.Profile()

    # Clear the cache before benchmarking to ensure clean metrics
    fib_cached.cache_clear()

    profile.enable()

    # Compare naive vs cached Fibonacci calculations for N=15
    fib_naive(15)
    fib_cached(15)

    profile.disable()

    # Sort statistics by cumulative time spent for each function call.
    # There are other ways to sort the stats by, but this is the most
    # common way of doing so. For more info, please consult Python docs:
    # https://docs.python.org/3/library/profile.html
    buffer = io.StringIO()
    ps = pstats.Stats(profile, stream=buffer).sort_stats("cumulative")

    # print_stats writes the tabular profiling info to the buffer
    ps.print_stats()
    output = buffer.getvalue()

    # Naive recursive fib(15) requires exactly 1,973 calls.
    # Cached recursive fib(15) requires exactly 16 calls (inputs 0 to 15).
    naive_called = any("1973" in line and "fib_naive" in line for line in output.split("\n"))
    cached_called = any("16" in line and "fib_cached" in line for line in output.split("\n"))

    assert naive_called is True
    assert cached_called is True


if __name__ == "__main__":
    main()
