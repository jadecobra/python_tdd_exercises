import datetime
import random
import sleep_duration
import unittest

def random_number(start, end, digits=2):
    return f'{random.randint(start, end):0{digits}}'



def get_random_timestamp():
    return (
        f'{random_number(0,9999,4)}/'
        f'{random_number(1,12)}/'
        f'{random_number(1,31)} '
        f'{random_number(0,23)}:'
        f'{random_number(0,59)}'
    )


def random_timestamp():
    result = get_random_timestamp()
    try:
        sleep_duration.get_datetime(result)
    except ValueError:
        return random_timestamp()
    else:
        return result


class TestSleepDuration(unittest.TestCase):

    def assertWakeTimeEarlier(
        self, wake_time=None, sleep_time=None
    ):
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        ):
            sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            )

    def test_get_datetime(self):
        timestamp = random_timestamp()
        self.assertEqual(
            sleep_duration.get_datetime(
                timestamp
            ),
            datetime.datetime.strptime(
                timestamp,
                '%Y/%m/%d %H:%M'
            )
        )

    def test_duration(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp()
        else:
            self.assertEqual(
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )


# Exceptions Encountered
# AssertionError
# TypeError
# NameError
# AttributeError
# ValueError