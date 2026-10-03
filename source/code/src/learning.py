def model(expectations, reality):
    if expectations > reality:
        return expectations + 1
    else:
        return reality + 1
