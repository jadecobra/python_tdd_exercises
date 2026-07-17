def logical_true():
    return True


def logical_false():
    return False


def logical_identity(the_input):
    return the_input


def logical_negation(the_input):
    return not the_input


def contradiction(first_input, input):
    return False


def logical_conjunction(first_input, second_input):
    return first_input and second_input


def project_second(first_input, second_input):
    return second_input


def converse_non_implication(first_input, second_input):
    return logical_conjunction(
        logical_negation(first_input),
        second_input
    )
    return not first_input and second_input