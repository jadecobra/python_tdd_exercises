import src.person


class WPass:

    pass


class WParentheses():

    pass


class WObject(object):

    pass


class Doe(src.person.Person):

    def __init__(self, first_name, last_name='doe'):
        super().__init__(first_name, last_name)


class Smith(src.person.Person):

    def __init__(self, first_name, last_name='smith'):
        super().__init__(first_name, last_name)


class Blow(src.person.Person):

    def __init__(self, first_name, last_name='blow'):
        super().__init__(first_name, last_name)


class Baby(Blow, Doe): pass


class Lil(Doe, Smith): pass