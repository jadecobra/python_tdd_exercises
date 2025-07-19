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


class Counter:
    def __init__(self):
        self.value = 0 # This is the "shared variable" for *this specific counter*

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value

# Now, you can create *multiple independent counters*
counter1 = Counter()
counter2 = Counter()

counter1.increment()
print(counter1.get_value()) # Output: 1

counter2.increment()
counter2.increment()
print(counter2.get_value()) # Output: 2

print(counter1.get_value()) # Output: 1 (counter1's value is distinct from counter2's)
