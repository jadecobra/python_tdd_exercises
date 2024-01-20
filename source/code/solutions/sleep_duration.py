import datetime

def get_datetime_object(timestamp):
    return datetime.datetime.strptime(
        timestamp, '%d/%m/%y %H:%M'
    )

def duration(wake_time=None, sleep_time=None):
    wake_time = get_datetime_object(wake_time)
    sleep_time = get_datetime_object(sleep_time)
    if wake_time > sleep_time:
        return str(wake_time - sleep_time)
    else:
        raise ValueError(
            f'wake_time: {wake_time} is earlier '
            f'than sleep_time: {sleep_time}'
        )