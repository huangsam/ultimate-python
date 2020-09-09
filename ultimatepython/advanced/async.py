import asyncio
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

# Module-level constants
_MILLISECOND = .001
_HOUR = 3600


@dataclass
class JobRecord:
    """Job record with useful metadata."""

    guid: str
    queued_at: datetime
    started_at: datetime


def _is_valid_record(record):
    """Check whether job record is valid or not."""
    return record.queued_at < record.started_at


def _current_time():
    """Return current time that is timezone-naive."""
    return datetime.now()


async def start_job(delay, job_id):
    """Start job_id after a certain delay in seconds."""
    queue_time = _current_time()
    await asyncio.sleep(delay)
    start_time = _current_time()
    return JobRecord(job_id, queue_time, start_time)


async def schedule_jobs():
    """Schedule jobs concurrently."""
    # Create a job which also represents a coroutine
    single_job = start_job(_MILLISECOND, uuid4().hex)
    assert asyncio.iscoroutine(single_job)

    # Grab a job record from the coroutine
    single_record = await single_job
    assert _is_valid_record(single_record)

    # Task is a wrapped coroutine which also represents a future
    single_task = asyncio.create_task(start_job(_HOUR, uuid4().hex))
    assert asyncio.isfuture(single_task)

    # Futures are different from coroutines in that they can be cancelled
    single_task.cancel()
    try:
        await single_task
    except asyncio.exceptions.CancelledError:
        assert single_task.cancelled()

    # Gather coroutines for batch start
    batch_jobs = [start_job(_MILLISECOND, uuid4().hex) for _ in range(10)]
    batch_records = await asyncio.gather(*batch_jobs)

    # We get the same amount of records as we have coroutines
    assert len(batch_records) == len(batch_jobs)
    assert all(_is_valid_record(record) for record in batch_records)


def main():
    asyncio.run(schedule_jobs())


if __name__ == "__main__":
    main()
