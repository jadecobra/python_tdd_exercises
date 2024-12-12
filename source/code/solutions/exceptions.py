def function_name():
    return None


def raise_exception():
    raise Exception('BOOM!')


def does_not_raise_exception():
    return None


def an_exception_handler(a_function):
    try:
        a_function()
    except Exception:
        return 'failed'
    else:
        return 'succeeded'