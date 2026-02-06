def logical_true():
    return True


def logical_false():
    return False


def logical_identity(the_input):
    return the_input


def logical_negation(the_input):
    return not the_input


def contradiction(first_input, second_input):
    return False


def logical_conjunction(first_input, second_input):
    return first_input and second_input


def project_second(first_input, second_input):
    return second_input


def converse_non_implication(first_input, second_input):
    return not first_input and second_input


def negate_first(first_input, second_input):
    return not first_input


def logical_nand(first_input, second_input):
    return not (first_input and second_input)


def tautology(first_input, second_input):
    return True


def logical_disjunction(first_input, second_input):
    return first_input or second_input


def exclusive_disjunction(first_input, second_input):
    return first_input != second_input
    return not first_input == second_input
    return (
        (not first_input and second_input)
        or
        (first_input and not second_input)
    )


def material_non_implication(first_input, second_input):
    return first_input and not second_input


def project_first(first_input, second_input):
    return first_input


def converse_implication(first_input, second_input):
    return first_input or not second_input


def negate_second(first_input, second_input):
    return not second_input


def logical_nor(first_input, second_input):
    return not (first_input or second_input)


def logical_equality(first_input, second_input):
    return first_input == second_input
    return (
        (first_input or not second_input)
        and
        (not first_input or second_input)
    )


def material_implication(first_input, second_input):
    return not first_input or second_input