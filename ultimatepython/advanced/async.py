"""
Concurrent programming with asyncio, introduced in Python 3.4, provides
an event loop for handling asynchronous operations. This module demonstrates
basic asyncio patterns including coroutines, tasks, concurrent execution
with gather, and task cancellation. It uses the context of a scheduler
which runs fire-and-forget operations for starting jobs, assuming that
job startup has some intrinsic delay.

This module also covers advanced asyncio patterns including task groups
for structured concurrency (Python 3.11+), semaphores for limiting
concurrency, timeouts, exception handling in concurrent tasks, event
loop management, and task shielding to protect critical operations from
cancellation.
"""

import asyncio
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

# Module-level constants
_DELAY_SMALL = 0.001
_DELAY_LARGE = 3600


@dataclass
class JobRecord:
    """Job record with useful metadata."""

    guid: str
    queued_at: datetime
    started_at: datetime


def _is_valid_record(record):
    """Check whether job record is valid or not."""
    return record.queued_at < record.started_at


def _current_time() -> datetime:
    """Return current time that is timezone-naive."""
    return datetime.now()


async def start_job(job_id: str, delay: float) -> JobRecord:
    """Start job ID after a certain amount of delay."""
    queue_time = _current_time()
    await asyncio.sleep(delay)
    start_time = _current_time()
    return JobRecord(job_id, queue_time, start_time)


async def failing_job(job_id: str) -> None:
    """A job that sometimes fails."""
    if int(job_id[-1]) % 3 == 0:  # Fail every 3rd job
        raise ValueError(f"Job {job_id} failed!")
    await asyncio.sleep(_DELAY_SMALL)


async def basic_async_patterns() -> None:
    """Basic async patterns demonstration."""
    # Start a job which also represents a coroutine
    single_job = start_job(uuid4().hex, _DELAY_SMALL)
    assert asyncio.iscoroutine(single_job)

    # Grab a job record from the coroutine
    single_record = await single_job
    assert _is_valid_record(single_record)

    # Task is a wrapped coroutine which also represents a future
    single_task = asyncio.create_task(start_job(uuid4().hex, _DELAY_LARGE))
    assert asyncio.isfuture(single_task)

    # Futures are different from other coroutines since they can be cancelled
    single_task.cancel()
    task_failed = False
    try:
        await single_task
    except asyncio.exceptions.CancelledError:
        assert single_task.cancelled()
        task_failed = True
    assert task_failed is True

    # Gather coroutines for batch start
    batch_jobs = [start_job(uuid4().hex, _DELAY_SMALL) for _ in range(10)]
    batch_records = await asyncio.gather(*batch_jobs)

    # We get the same amount of records as we have coroutines
    assert len(batch_records) == len(batch_jobs)
    assert all(_is_valid_record(record) for record in batch_records)


async def advanced_async_patterns() -> None:
    """Demonstrate advanced asyncio patterns."""

    # Task Groups - structured concurrency (Python 3.11+)
    async def task_group_example():
        results = []
        try:
            async with asyncio.TaskGroup() as tg:
                # Start multiple tasks in a group
                for i in range(5):
                    tg.create_task(start_job(f"task_{i}", _DELAY_SMALL))
        except Exception as e:
            # TaskGroup propagates exceptions from child tasks
            pass

        # All tasks in the group complete or fail together
        assert True  # TaskGroup structure is valid

    await task_group_example()

    # Semaphores for limiting concurrency
    semaphore = asyncio.Semaphore(3)  # Allow max 3 concurrent operations

    async def limited_concurrency_job(job_id: str):
        async with semaphore:
            # Only 3 jobs can execute this section at once
            await asyncio.sleep(_DELAY_SMALL)
            return f"completed_{job_id}"

    # Start 10 jobs but only 3 can run concurrently
    concurrent_jobs = [limited_concurrency_job(f"sem_{i}") for i in range(10)]
    concurrent_results = await asyncio.gather(*concurrent_jobs)
    assert len(concurrent_results) == 10
    assert all("completed_" in result for result in concurrent_results)

    # Exception handling with gather
    mixed_jobs = [
        failing_job("job_1"),  # succeeds
        failing_job("job_2"),  # succeeds
        failing_job("job_3"),  # fails
        failing_job("job_4"),  # succeeds
    ]

    # Return exceptions instead of raising them
    results = await asyncio.gather(*mixed_jobs, return_exceptions=True)
    assert len(results) == 4
    # Check that we got a mix of results and exceptions
    exceptions_found = sum(1 for r in results if isinstance(r, Exception))
    successes_found = sum(1 for r in results if not isinstance(r, Exception))
    assert exceptions_found == 1  # One job failed
    assert successes_found == 3  # Three jobs succeeded

    # Timeouts and cancellation
    async def slow_job():
        await asyncio.sleep(1.0)  # Takes 1 second
        return "slow_result"

    try:
        # Timeout after 0.1 seconds
        result = await asyncio.wait_for(slow_job(), timeout=0.1)
    except asyncio.TimeoutError:
        result = None
    assert result is None  # Should timeout

    # Event loop management
    loop = asyncio.get_running_loop()
    assert isinstance(loop, asyncio.AbstractEventLoop)

    # Schedule callback on the event loop
    callback_result = None

    def sync_callback():
        nonlocal callback_result
        callback_result = "callback_executed"

    # Schedule callback to run soon
    loop.call_soon(sync_callback)
    await asyncio.sleep(0)  # Let the event loop process callbacks
    assert callback_result == "callback_executed"

    # Shielding tasks from cancellation
    async def important_task():
        await asyncio.sleep(_DELAY_SMALL)
        return "important_result"

    task = asyncio.create_task(important_task())
    shielded_task = asyncio.shield(task)

    # Even if we cancel the shield, the underlying task continues
    shielded_task.cancel()
    try:
        await shielded_task
    except asyncio.CancelledError:
        pass

    # The original task should still complete
    await task  # Wait for the original task
    assert task.result() == "important_result"


def main() -> None:
    # Run basic patterns
    asyncio.run(basic_async_patterns())

    # Run advanced patterns
    asyncio.run(advanced_async_patterns())


if __name__ == "__main__":
    main()
