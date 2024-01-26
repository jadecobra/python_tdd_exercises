import datetime
import random
import sleep_duration
import unittest


class TestSleepDuration(unittest.TestCase):

    def test_string_methods_and_attributes(self):
        self.maxDiff = None
        self.assertEqual(
            dir("00:00"),
            [
                '__add__',
                '__class__',
                '__contains__',
                '__delattr__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__format__',
                '__ge__',
                '__getattribute__',
                '__getitem__',
                '__getnewargs__',
                '__getstate__',
                '__gt__',
                '__hash__',
                '__init__',
                '__init_subclass__',
                '__iter__',
                '__le__',
                '__len__',
                '__lt__',
                '__mod__',
                '__mul__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__rmod__',
                '__rmul__',
                '__setattr__',
                '__sizeof__',
                '__str__',
                '__subclasshook__',
                'capitalize',
                'casefold',
                'center',
                'count',
                'encode',
                'endswith',
                'expandtabs',
                'find',
                'format',
                'format_map',
                'index',
                'isalnum',
                'isalpha',
                'isascii',
                'isdecimal',
                'isdigit',
                'isidentifier',
                'islower',
                'isnumeric',
                'isprintable',
                'isspace',
                'istitle',
                'isupper',
                'join',
                'ljust',
                'lower',
                'lstrip',
                'maketrans',
                'partition',
                'removeprefix',
                'removesuffix',
                'replace',
                'rfind',
                'rindex',
                'rjust',
                'rpartition',
                'rsplit',
                'rstrip',
                'split',
                'splitlines',
                'startswith',
                'strip',
                'swapcase',
                'title',
                'translate',
                'upper',
                'zfill'
            ]
        )

    def test_splitting_a_string(self):
        self.assertEqual(
            "01:23".split(':'),
            ['01', '23']
        )
        self.assertEqual(
            "12:34".split(':')[0],
            '12'
        )
        self.assertEqual(
            "12:34".split(':')[1],
            '34'
        )
        self.assertEqual(
            "21/11/06 16:40".split(':')[0],
            '21/11/06 16'
        )

    def test_floor_division(self):
        self.assertEqual(5//2, 2)

    def test_modulo_division(self):
        self.assertEqual(5%2, 1)

    def test_converting_a_string_to_an_integer(self):
        self.assertEqual(int("12"), 12)

    def test_datetime_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "21/11/06 16:30",
                "%d/%m/%y %H:%M"
            ),
            datetime.datetime(2006, 11, 21, 16, 30)
        )

    def test_subtracting_datetime_datetime_objects(self):
        sleep_time = datetime.datetime.strptime(
            "21/11/06 16:30",
            "%d/%m/%y %H:%M"
        )
        wake_time = datetime.datetime.strptime(
            "21/11/06 17:30",
            "%d/%m/%y %H:%M"
        )
        self.assertEqual(
            wake_time-sleep_time,
            datetime.timedelta(seconds=3600)
        )

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=7200)),
            "2:00:00"
        )

    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minutes = random.randint(0, 59)
        sleep_minutes = random.randint(0, 59)

        wake_time = f'21/11/06 {wake_hour}:{wake_minutes}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minutes}'
        pattern = '%d/%m/%y %H:%M'

        difference = (
            datetime.datetime.strptime(wake_time, pattern)
          - datetime.datetime.strptime(sleep_time, pattern)
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
            pass

# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError
# ValueError