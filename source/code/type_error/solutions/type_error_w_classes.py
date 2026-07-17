def none(): return None
def false(): return False
def true(): return True
def an_integer(): return 1234
def a_float(): return 5.678
def a_string(): return 'a string'
def a_tuple(): return (0, 1, 2, 'n')
def a_list(): return [0, 1, 2, 'n']
def a_set(): return {0, 1, 2, 'n'}
def a_dictionary(): return {'key': 'value'}


def function_00(the_input):
    return None


def function_01(first, second):
    return None


def function_02(
    third, second, first
):
    return None


def function_03(
    first, second, third, fourth,
):
    return None


def function_04(argument):
    return None


def function_05(argument_0, argument_1):
    return None


def function_06(argument_0, argument_1, argument_2):
    return None


def function_07(
    argument_0, argument_1,
    argument_2, argument_n
):
    return None


def function_08(name, argument):
    return None


class AClass(object):

    @staticmethod
    def method_00(): return None

    @staticmethod
    def method_01(): return None

    def method_02(self):
        return self.method_01()

    @staticmethod
    def method_03():
        return AClass().method_02()

    @staticmethod
    def method_04():
        return AClass.method_02(AClass)

    def method_05(self):
        return self.method_02()

    def method_06(self):
        return self.method_01()

    def method_07(self):
        return self.method_00()

    def method_08(self):
        return self.method_04()

    def method_09(self):
        return self.method_03()