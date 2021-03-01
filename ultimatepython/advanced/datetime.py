from datetime import datetime, timezone


def convert_dt_to_utc_epoch(dt):
    """Convert datetime to UTC time in epoch seconds."""
    return dt.timestamp()


def convert_utc_epoch_to_dt(epoch):
    """Convert epoch seconds to datetime."""
    return datetime.fromtimestamp(epoch, tz=timezone.utc)


def get_utc_now_as_dt():
    """Get current UTC time as datetime."""
    return datetime.now(tz=timezone.utc)


def get_utc_now_as_epoch():
    """Get current UTC time as epoch seconds."""
    return convert_dt_to_utc_epoch(get_utc_now_as_dt())


def main():
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

    # Cannot compute difference between offset-naive and offset-aware
    # datetime objects
    calc_failed = False
    try:
        _ = utc_dt - naive_dt
    except TypeError:
        calc_failed = True
    assert calc_failed is True

    # Create new UTC time as datetime
    utc_dt_new_one = get_utc_now_as_dt()
    assert utc_dt_new_one > utc_dt

    # Create another new UTC time as epoch seconds
    utc_epoch_new_two = get_utc_now_as_epoch()
    utc_epoch_new_one = convert_dt_to_utc_epoch(utc_dt_new_one)

    # Epoch seconds line up as expected
    assert utc_epoch_new_two > utc_epoch_new_one > naive_dt_epoch


if __name__ == "__main__":
    main()
