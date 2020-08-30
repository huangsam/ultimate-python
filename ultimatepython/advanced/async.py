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


def current_time():
    """Return current time that is timezone-naive."""
    return datetime.now()


async def start_job(delay, job_id):
    """Start task_id after a certain delay in seconds."""
    queue_time = current_time()
    print(f"{queue_time} -> Queue job {job_id[:16]}...")
    await asyncio.sleep(delay)
    start_time = current_time()
    print(f"{start_time} -> Start job {job_id[:16]}...")
    return JobRecord(job_id, queue_time, start_time)


async def schedule_jobs():
    """Schedule jobs concurrently."""
    print(f"{current_time()} -> Send kickoff email")

    # Create a single job
    single_job = start_job(_MILLISECOND, uuid4().hex)
    assert asyncio.iscoroutine(single_job)

    # Grab a single record from the job
    single_record = await single_job
    assert isinstance(single_record, JobRecord)

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
    batch_jobs = [start_job(.01, uuid4().hex) for _ in range(10)]
    batch_records = await asyncio.gather(*batch_jobs)

    # We get the same amount of records as we have coroutines
    assert len(batch_records) == len(batch_jobs)

    for record in batch_records:
        assert isinstance(record, JobRecord)
        assert record.queued_at < record.started_at

    print(f"{current_time()} -> Send confirmation email")


def main():
    asyncio.run(schedule_jobs())


if __name__ == "__main__":
    main()
