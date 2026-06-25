def joe():
    return 'joe, blow, M, 1996'


def jane():
    return 'jane, doe, F, 1991'


def john():
    return 'john, smith, M, 1580'


def mary():
    return 'mary, public, F, 2000'


def test_joe():
    assert joe() == 'joe, blow, M, 1996'


def test_jane():
    assert jane() == 'jane, doe, F, 1991'


def test_john():
    assert john() == 'john, smith, M, 1580'


def test_mary():
    assert mary() == 'mary, public, F, 2000'


# Exceptions seen
# AssertionError
# NameError
# TypeError