import src.person


class Doe(src.person.Person):

    def __init__(self, first_name):
        super().__init__(first_name)


class Blow(src.person.Person):

    def __init__(self, first_name):
        super().__init__(
            first_name=first_name,
            last_name='blow',
        )


class Smith(src.person.Person):

    eye_color = 'brown'

    def __init__(self, first_name):
        super().__init__(
            first_name=first_name,
            last_name='smith',
        )


class Jane(Doe):

    def __init__(
            self, first_name='jane',
            last_name=None
        ):
        super().__init__(first_name)
        self.eye_color = 'green'


class Joe(Blow):

    def __init__(self, first_name='joe'):
        super().__init__(first_name)
        self.eye_color = 'blue'


class Mary(Joe, Jane):

    def __init__(
            self, first_name='mary',
            last_name=None,
        ):
        super().__init__(first_name)


class John(Smith):

    def __init__(self, first_name='john'):
        super().__init__(first_name)


class Lil(Mary, John):

    def __init__(self):
        super().__init__('lil')