def function_name():
    return None


def raise_exception():
    raise Exception('BOOM!')


def does_not_raise_exception():
    return None


def exception_handler(function):
    try:
        function()
    except Exception:
        return 'failed'
    else:
        return 'succeeded'