import src.type_error


def test_type_error_w_positional_arguments():
    src.type_error.function_00('a')
    src.type_error.function_01('a', 'b')
    src.type_error.function_02('a', 'b', 'c')
    src.type_error.function_03('a', 'b', 'c', 'd')
    src.type_error.function_04('a')
    src.type_error.function_05('a', 'b')
    src.type_error.function_06('a', 'b', 'c')
    src.type_error.function_07('a', 'b', 'c', 'd')
    src.type_error.function_08('last', 'one')


def test_type_error_w_keyword_arguments():
    src.type_error.function_00(the_input=0)
    src.type_error.function_01(
        first='first',
        second={'key': 'value'},
    )
    src.type_error.function_02(
        third=(0, 1, 2, 'n'),
        second=[0, 1, 2, 'n'],
        first={0, 1, 2, 'n'},
    )
    src.type_error.function_03(
        first=None,
        second=False,
        third=True,
        fourth=4,
    )
    src.type_error.function_04(argument='value')
    src.type_error.function_05(
        argument_0='value1',
        argument_1=(0, 1, 2, 'n'),
    )
    src.type_error.function_06(
        argument_0='value1',
        argument_1=(0, 1, 2, 'n'),
        argument_2=[0, 1, 2, 'n'],
    )
    src.type_error.function_07(
        argument_0=(0, 1, 2, 'n'),
        argument_1=[0, 1, 2, 'n'],
        argument_2={0, 1, 2, 'n'},
        argument_n={'key': 'value'},
    )
    src.type_error.function_08(
        argument='positional', name='keyword'
    )


def test_type_error_w_args_and_kwargs():
    src.type_error.function_00('argument')
    src.type_error.function_01(1, 0)
    src.type_error.function_02(
        third=True, second=False, first=None
    )
    src.type_error.function_03(
        second=[0, 1, 2, 'n'],
        first=(0, 1, 2, 'n'),
        third={0, 1, 2, 'n'},
        fourth={'key': 'value'}
    )
    src.type_error.function_04('value')
    src.type_error.function_05(
        (0, 1, 2, 'n'),
        [0, 1, 2, 'n'],
    )
    src.type_error.function_06(
        (0, 1, 2, 'n'),
        [0, 1, 2, 'n'],
        argument_2={0, 1, 2, 'n'},
    )
    src.type_error.function_07(
        argument_n={'key': 'value'},
        argument_2={0, 1, 2, 'n'},
        argument_0=(0, 1, 2, 'n'),
        argument_1=[0, 1, 2, 'n'],
    )
    src.type_error.function_08(
        'positional', argument='keyword'
    )


def test_type_error_w_class_methods():
    src.type_error.AClass.method_00()
    src.type_error.AClass().method_01()
    src.type_error.AClass().method_02()
    src.type_error.AClass.method_03()
    src.type_error.AClass.method_04()
    src.type_error.AClass().method_05()
    src.type_error.AClass().method_06()
    src.type_error.AClass().method_07()
    src.type_error.AClass().method_08()
    src.type_error.AClass().method_09()


# Exceptions seen
# AssertionError
# NameError
# TypeError
# ModuleNotFoundError
# AttributeError