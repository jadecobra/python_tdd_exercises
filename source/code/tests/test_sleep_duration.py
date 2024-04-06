import datetime
import random
import sleep_duration
import unittest

def get_random_timestamp(date):
    return f'{date} {random.randint(0,23):02}:{random.randint(0,59):02}'


class TestSleepDuration(unittest.TestCase):

    def test_string_splitting(self):
        split = '01:23'.split(':')

        self.assertEqual(split, ['01', '23'])
        self.assertEqual(split[0], '01')
        self.assertEqual(split[1], '23')

        self.assertEqual(
            '31/12/99 13:04'.split(':')[0],
            '31/12/99 13'
        )

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('31/12/99 13')

    def test_floor_aka_integer_division(self):
        self.assertEqual(120//60, 2)
        self.assertEqual(150//60, 2)

    def test_the_modulo_operation(self):
        self.assertEqual(120%60, 0)
        self.assertEqual(150%60, 30)

    def test_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "21/11/06 16:30",
                "%d/%m/%y %H:%M"
            ),
            datetime.datetime(2006, 11, 21, 16, 30)
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

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=7654)),
            '2:07:34'
        )

    def test_duration_w_earlier_wake_than_sleep_time(self):
        wake_time = '21/12/12 01:00'
        sleep_time = '21/12/12 02:00'

        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time} is earlier '
            f'than sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

    def test_duration_w_date_and_time(self):
        wake_time = get_random_timestamp('31/12/99')
        sleep_time = get_random_timestamp('31/12/99')

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
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )


# Exceptions Encountered
# AssertionError
# TypeError
# NameError
# AttributeError
# ValueError
