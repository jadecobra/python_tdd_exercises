class WithPass:
    pass


class WithParentheses():
    pass


class WithObject(object):
    pass


class WithAttributes(object):

    attribute_a = 'attribute_a'
    attribute_b = 'attribute_b'
    attribute_c = 'attribute_c'
    attribute_d = 'attribute_d'


class WithMethods(object):

    def method_a():
        return 'You called method_a'


    def method_b():
        return 'You called method_b'

    def method_c():
        return 'You called method_c'

    def method_d():
        return 'You called method_d'


class WithAttributesAndMethods(object):

    attribute = 'attribute'

    def method():
        return 'You called method'


class Human(object):

    def __init__(self, sex='M'):
        self.sex = sex


class Boy(Human): pass


class Girl(Human): pass


class Other(Boy): pass