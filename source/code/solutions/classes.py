import datetime


def factory(
        first_name, last_name='doe',
        sex='M', year_of_birth=None
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': datetime.datetime.today().year - year_of_birth,
    }


def introduce(person):
    return f'Hi! My name is {person.get("first_name").title()} {person.get("last_name").title()}, I am {person.get("age")} years old'


def update_birthday(person, birthday):
    person.update(birthday='June 2nd')
    return person



class Person(object):

    def __init__(self, first_name, last_name='doe', year_of_birth=datetime.datetime.today().year, sex='M'):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.year_of_birth = year_of_birth

    @staticmethod
    def today():
        return datetime.datetime.today()

    def get_age(self):
        return self.today().year - self.year_of_birth

    def introduce(self):
        return f'Hi! My name is {self.first_name.title()} {self.last_name.title()}, I am {self.get_age()} years old'

    def add_birthday(self, birthday=None):
        if not birthday:
            day = self.today().day
            month = self.today().day
            self.birthday = f'{day}/{month}'
        else:
            self.birthday = birthday

    def get_birthday(self):
        try:
            return self.birthday
        except AttributeError:
            self.add_birthday()
            return self.birthday

    def to_dict(self):
        return dict(
            first_name=self.first_name,
            last_name=self.last_name,
            age=self.get_age(),
            birthday=self.get_birthday(),
            sex=self.sex,
        )