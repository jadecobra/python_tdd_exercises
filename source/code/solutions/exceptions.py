def function():
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


def always_returns(function):
    try:
        function()
    except Exception:
        return 'failed'
    else:
        return 'succeeded'
    finally:
        return 'always returns this'