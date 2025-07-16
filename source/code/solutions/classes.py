class WithPass:
    pass


class WithParentheses():
    pass


class WithObject(object):
    pass


class WithAttributes(object):

    attribute = 'attribute'


class WithMethods(object):

    def method():
        return 'You called method'


class WithAttributesAndMethods(object):

    attribute = 'attribute'

    def method():
        return 'You called method'


class Human(object):

    def __init__(self, sex='M'):
        self.sex = sex


class Boy(Human): pass


class Girl(Human): pass


class Other(Human): pass