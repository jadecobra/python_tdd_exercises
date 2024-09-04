def model(expectations, reality):
    if expectations > reality:
        return expectations + 1
    else:
        return reality + 1


def model(expectations, reality):
    if expectations <= reality:
        return reality + 1
    else:
        return expectations + 1
