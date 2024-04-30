import datetime


def get_datetime(timestamp):
    return datetime.datetime.strptime(
        timestamp, '%d/%m/%y %H:%M'
    )


def duration(wake_time, sleep_time):
    if wake_time < sleep_time:
        raise ValueError(
            f"wake_time: "{wake_time}""
            " is earlier than "
            f"sleep_time: "{sleep_time}""
        )
    else:
        return str(
            get_datetime(wake_time)
          - get_datetime(sleep_time)
        )
