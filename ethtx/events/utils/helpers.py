import datetime


def utc_timestamp_to_id() -> int:
    dt = datetime.datetime.now(datetime.timezone.utc)

    utc_time = dt.replace(tzinfo=datetime.timezone.utc)
    utc_timestamp = utc_time.timestamp()

    return int(utc_timestamp)
