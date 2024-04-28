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
            f'wake_time: {wake_time}'
            ' is earlier than '
            f'sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
        self.assertWakeTimeEarlier(
            wake_time='31/12/99 01:00',
            sleep_time='31/12/99 02:00',
        )

    def test_duration(self):
        wake_time = random_timestamp('31/12/99')
        sleep_time = random_timestamp('30/12/99')

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
        )

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )
        except ValueError:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )


# Exceptions Encountered
# AssertionError
# TypeError
# NameError
# AttributeError
# ValueError