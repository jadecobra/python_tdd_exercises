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

    def test_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "21/11/06 16:30",
                "%d/%m/%y %H:%M"
            ),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

    def test_subtracting_datetime_objects(self):
        pattern = "%d/%m/%y %H:%M"
        sleep_time = datetime.datetime.strptime(
            "21/11/06 16:30", pattern
        )
        wake_time = datetime.datetime.strptime(
            "21/11/06 17:30", pattern
        )

        self.assertEqual(
            wake_time-sleep_time,
            datetime.timedelta(seconds=3600)
        )

    def test_converting_timedelta_to_a_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=1234)),
            '0:20:34'
        )

    def assertWakeTimeEarlier(self, wake_time=None, sleep_time=None):
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
            sleep_time='31/12/99 02:00'
        )

    def test_duration_w_hours_and_minutes(self):
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