def function_w_pass():
    pass


def function_w_none():
    return


def function_w_return_none():
    return None


def singleton():
    return 'the same thing'


def singleton_w_inputs(*args):
    return singleton()


def passthrough(argument):
    return argument