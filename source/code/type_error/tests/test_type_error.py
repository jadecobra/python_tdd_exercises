def function_00(the_input):
    return None


def function_01(first, second):
    return None


def function_02(first, second, third):
    return None


def function_03(first, second, third, fourth):
    return None


def function_04(argument):
    return None


def function_05(argument_0, argument_1):
    return None


def function_06(
    argument_0, argument_1,
    argument_2,
):
    return None


def function_07(
    argument_0, argument_1,
    argument_2, argument_n
):
    return None


def function_08(name, argument):
    return None


def test_type_error_w_positional_arguments():
    function_00('a')
    function_01('a', 'b')
    function_02('a', 'b', 'c')
    function_03('a', 'b', 'c', 'd')
    function_04('a')
    function_05('a', 'b')
    function_06('a', 'b', 'c')
    function_07('a', 'b', 'c', 'd')
    function_08('last', 'one')


def test_type_error_w_keyword_arguments():
    function_00(the_input=0)
    function_01(
        first='first',
        second={'key': 'value'},
    )
    function_02(
        third=(0, 1, 2, 'n'),
        second=[0, 1, 2, 'n'],
        first={0, 1, 2, 'n'},
    )
    function_03(
        first=None,
        second=False,
        third=True,
        fourth=4,
    )
    function_04(argument='value')
    function_05(
        argument_0='value_1',
        argument_1=(0, 1, 2, 'n'),
    )
    function_06(
        argument_0='value1',
        argument_1=(0, 1, 2, 'n'),
        argument_2=[0, 1, 2, 'n'],
    )
    function_07(
        argument_0=(0, 1, 2, 'n'),
        argument_1=[0, 1, 2, 'n'],
        argument_2={0, 1, 2, 'n'},
        argument_n={'key': 'value'},
    )
    function_08(
        argument='positional',
        name='keyword',
    )


def test_type_error_w_args_and_kwargs():
    function_00('argument')
    function_01(1, 0)
    function_02(
        third=True, second=False,
        first=None,
    )
    function_03(
        second=[0, 1, 2, 'n'],
        first=(0, 1, 2, 'n'),
        third={0, 1, 2, 'n'},
        fourth={'key': 'value'},
    )
    function_04('value')
    function_05(
        (0, 1, 2, 'n'),
        [0, 1, 2, 'n'],
    )
    function_06(
        (0, 1, 2, 'n'),
        [0, 1, 2, 'n'],
        argument_2={0, 1, 2, 'n'},
    )
    function_07(
        argument_n={'key': 'value'},
        argument_2={0, 1, 2, 'n'},
        argument_0=(0, 1, 2, 'n'),
        argument_1=[0, 1, 2, 'n'],
    )
    function_08(
        'positional',
        argument='keyword',
    )


# Exceptions seen
# AssertionError
# NameError
# TypeError