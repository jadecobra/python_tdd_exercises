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

    def assertWakeTimeEarlier(self, wake_time, sleep_time):
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

    @staticmethod
    def get_datetime(wake_time):
        return datetime.datetime.strptime(
            wake_time, '%d/%m/%y %H:%M'
        )

    def test_duration(self):
        wake_time = random_timestamp('31/12/99')
        sleep_time = random_timestamp('31/12/99')

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time, sleep_time
            )
            wake_time = random_timestamp('31/12/99')
        else:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(
                    self.get_datetime(wake_time)
                  - self.get_datetime(sleep_time)
                )
            )


# Exceptions Encountered
# AssertionError
# TypeError
# NameError
# AttributeError
# ValueError