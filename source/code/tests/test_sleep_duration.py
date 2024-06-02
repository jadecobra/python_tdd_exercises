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
        timestamp = random_timestamp('2006/11/21')
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
        sleep_date = '1999/12/31'
        sleep_time = random_timestamp(sleep_date)
        wake_time = random_timestamp('1999/12/30')

        while (
            sleep_duration.get_datetime(wake_time)
          < sleep_duration.get_datetime(sleep_time)
        ):
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                sleep_date
            )
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