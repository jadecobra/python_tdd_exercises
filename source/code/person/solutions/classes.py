import src.person


class WPass: pass


class WParentheses(): pass


class WObject(object): pass


class Doe(src.person.Person): pass


class Blow(src.person.Person):

    def __init__(self, first_name):
        super().__init__(first_name, last_name='blow')


class Smith(src.person.Person):

    def __init__(self, first_name):
        super().__init__(first_name, last_name='smith')


class Jane(Doe):

    def __init__(self, first_name='jane', **kwargs):
        super().__init__(first_name=first_name)


class Joe(Blow):

    def __init__(self, first_name='joe'):
        super().__init__(first_name=first_name)


class Mary(Jane, Joe):

    def __init__(self, first_name='mary', **kwargs):
        super().__init__(first_name=first_name)


class John(Smith):

    def __init__(self, first_name='john', **kwargs):
        super().__init__(first_name=first_name)


class Lil(Mary, John):

    def __init__(self, first_name='lil'):
        super().__init__(first_name=first_name)