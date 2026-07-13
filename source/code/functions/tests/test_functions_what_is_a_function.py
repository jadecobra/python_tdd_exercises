def test_making_a_function_w_pass():
    def w_pass():
        pass

    assert w_pass() is None


def test_making_a_function_w_return():
    def w_return():
        return

    assert w_return() is None


def test_making_a_function_w_return_none():
    def w_return_none():
        return None

    assert w_return_none() is None


def test_what_happens_after_functions_return():
    def return_leaves_the_function():
        return None
        return 'only one way for this line to run'

    assert return_leaves_the_function() is None


def test_constant_function():
    def constant():
        return 'the same thing'

    assert constant() == 'the same thing'


# Exceptions seen
# AssertionError
# NameError
# TypeError