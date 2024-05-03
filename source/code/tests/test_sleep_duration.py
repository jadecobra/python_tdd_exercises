import datetime
import random
import sleep_duration
import unittest


def random_timestamp(date):
    return (
        f'{date} '
        f'{random.randint(0,23):02}:'
        f'{random.randint(0,59):02}'
    )


class TestSleepDuration(unittest.TestCase):

    def test_get_datetime(self):
        timestamp = random_timestamp('31/12/99')
        self.assertEqual(
            sleep_duration.get_datetime(
                timestamp
            ),
            datetime.datetime.strptime(
                timestamp, '%d/%m/%y %H:%M'
            )
        )

    def assertWakeTimeEarlier(self, wake_time=None, sleep_time=None):
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

    def test_duration(self):
        sleep_time = random_timestamp('31/12/99')
        wake_time = random_timestamp('31/12/99')

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                '31/12/99'
            )
        else:
            difference = (
                sleep_duration.get_datetime(
                    wake_time
                )
              - sleep_duration.get_datetime(
                    sleep_time
                )
            )
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )


# Exceptions Encountered
# AssertionError
# TypeError
# NameError
# AttributeError
# ValueError