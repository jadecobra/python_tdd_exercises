import datetime


def get_datetime(timestamp):
    return datetime.datetime.strptime(
        timestamp, "%Y/%m/%d %H:%M"
    )


def duration(wake_time=None, sleep_time=None):
    if wake_time < sleep_time:
        raise ValueError(
            f'wake_time: "{wake_time}"'
            " is earlier than "
            f'sleep_time: "{sleep_time}"'
        )
    else:
        return str(
            get_datetime(wake_time)
          - get_datetime(sleep_time)
        )
