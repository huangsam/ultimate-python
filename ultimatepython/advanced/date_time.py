"""
The `datetime` class is one of the core classes we encounter when tracking
events at a given date and time. By default, creating an instance with
`datetime.now` means that an offset-naive datetime object is produced in
the host's local timezone.

An offset-naive `datetime` object is useful for scripts that are run on a
personal device. Once we use `datetime` objects for web applications that
are deployed globally, it's important to know the offset that `datetime`
objects are aligned to before processing them. For more on `datetime`:

https://docs.python.org/3/library/datetime.html

Backend developers address this by storing time fields with offsets aligned
with the UTC (Coordinated Universal Time) timezone. As a result, time fields
can be displayed in any timezone - at any moment. For more on UTC:

https://en.wikipedia.org/wiki/Coordinated_Universal_Time

In this module, we will show the difference between offset-naive and
offset-aware `datetime` objects. We will also highlight the builtin
UTC timezone and show how it can be used to make the default `datetime`
object more powerful.
"""

from datetime import datetime, timezone


def convert_dt_to_utc_epoch(dt: datetime) -> int:
    """Convert datetime to UTC epoch seconds.

    Note that the timestamp method assumes that an offset-naive
    datetime instance is in the local timezone and converts its
    offset to UTC before making it a floating point number.
    """
    return dt.timestamp()


def convert_utc_epoch_to_dt(epoch: int) -> datetime:
    """Convert UTC epoch seconds to datetime."""
    return datetime.fromtimestamp(epoch, tz=timezone.utc)


def convert_dt_timezone(dt: datetime, tz: timezone) -> datetime:
    """Convert datetime timezone."""
    return dt.astimezone(tz=tz)


def get_utc_now_as_dt() -> datetime:
    """Get current UTC time as datetime."""
    return datetime.now(tz=timezone.utc)


def get_utc_now_as_epoch() -> int:
    """Get current UTC time as epoch seconds."""
    return convert_dt_to_utc_epoch(get_utc_now_as_dt())


def main() -> None:
    # Create offset-naive datetime
    naive_dt = datetime.now()
    assert naive_dt.tzinfo is None

    # Change offset-naive datetime to epoch seconds
    naive_dt_epoch = convert_dt_to_utc_epoch(naive_dt)
    assert naive_dt_epoch > 0

    # Change epoch seconds to UTC datetime
    utc_dt = convert_utc_epoch_to_dt(naive_dt_epoch)
    assert utc_dt.tzinfo is timezone.utc
    assert convert_dt_to_utc_epoch(utc_dt) == naive_dt_epoch

    # We cannot compute differences between offset-naive and offset-aware
    # datetime objects
    calc_failed = False
    try:
        _ = utc_dt - naive_dt
    except TypeError:
        calc_failed = True
    assert calc_failed is True

    # But we can change the timezone of an offset-naive datetime object
    # first before running operations on them
    assert convert_dt_timezone(naive_dt, timezone.utc) == utc_dt

    # Create new UTC time as datetime
    utc_dt_new_one = get_utc_now_as_dt()
    assert utc_dt_new_one > utc_dt

    # Create another new UTC time as epoch seconds
    utc_epoch_new_two = get_utc_now_as_epoch()
    utc_epoch_new_one = convert_dt_to_utc_epoch(utc_dt_new_one)
    assert utc_epoch_new_two > utc_epoch_new_one > naive_dt_epoch
    utc_dt_new_two = convert_utc_epoch_to_dt(utc_epoch_new_two)
    assert utc_dt_new_two > utc_dt_new_one > utc_dt


if __name__ == "__main__":
    main()
