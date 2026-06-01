import src.person


class WPass: pass


class WParentheses(): pass


class WObject(object): pass


class Doe(src.person.Person): pass


class Blow(src.person.Person):

    # def __init__(self, first_name):
    def __init__(self, first_name, **kwargs):
        super().__init__(first_name, last_name='blow')


class Smith(src.person.Person):

    # def __init__(self, first_name):
    def __init__(self, first_name, **kwargs):
        super().__init__(first_name, last_name='smith')


class Jane(Doe):

    # def __init__(self, first_name='jane'):
    def __init__(self, first_name='jane', **kwargs):
        # super().__init__(first_name=first_name)
        super().__init__(first_name=first_name, **kwargs)


class Joe(Blow):

    # def __init__(self, first_name='joe'):
    def __init__(self, first_name='joe', **kwargs):
        # super().__init__(first_name=first_name)
        super().__init__(first_name=first_name, **kwargs)


# class Mary(Jane): pass
# class Mary(Joe, Jane): pass
# class Mary(Jane, Joe): pass
class Mary(Joe, Jane):

    def __init__(self, first_name='mary'):
        super().__init__(first_name=first_name)


class John(Smith):

    # def __init__(self, first_name='john'):
    def __init__(self, first_name='john', **kwargs):
        # super().__init__(first_name=first_name)
        super().__init__(first_name=first_name, **kwargs)


class Lil(Mary, John):
# class Lil(John, Mary):

    def __init__(self, first_name='lil'):
        super().__init__(first_name=first_name)