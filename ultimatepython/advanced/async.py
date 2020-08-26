import asyncio
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class JobRecord:
    """Job record with useful metadata."""

    tid: int
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


async def start_batch():
    """Start a batch of jobs concurrently.

    Each item in the `tasks` list is a `asyncio.Task` instance. Each task
    was created by passing a coroutine instance (created by `start_job`)
    into the `asyncio.create_task` function.

    After awaiting the list of tasks, we get a list of `JobRecord` items
    with reasonable timestamps for queueing and starting.
    """
    print(f"{current_time()} -> Send kickoff email")

    tasks = [asyncio.create_task(start_job(i * .01, uuid4().hex))
             for i in range(1, 5)]

    # All tasks are instances of Task. They are also instances of Future
    # which is important because their completions can be deferred as
    # we will see in the next statement
    assert all(isinstance(task, asyncio.Task)
               and isinstance(task, asyncio.Future)
               for task in tasks)

    # Gather all `Task` instances for batch start
    job_records = await asyncio.gather(*tasks)
    for record in job_records:
        assert isinstance(record, JobRecord)
        assert record.queued_at < record.started_at

    print(f"{current_time()} -> Send confirmation email")


def main():
    asyncio.run(start_batch())


if __name__ == "__main__":
    main()
