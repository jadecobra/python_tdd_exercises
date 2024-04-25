import datetime


def get_datetime_object(timestamp):
    return datetime.datetime.strptime(
        timestamp, '%d/%m/%y %H:%M'
    )


def duration(wake_time=None, sleep_time=None):
    wake_datetime = get_datetime_object(
        wake_time
    )
    sleep_datetime = get_datetime_object(
        sleep_time
    )

    if wake_datetime < sleep_datetime:
        raise ValueError(
            f'wake_time: {wake_time}'
            ' is earlier than '
            f'sleep_time: {sleep_time}'
        )
    else:
        return str(
            wake_datetime
          - sleep_datetime
        )