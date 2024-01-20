def tree(number):
    star_generator = (
        "".join(("X" for i in range(i)))
        for i in range(number // 2, 0, -1)
    )
    return [
        f"{stars}"
        f"{'*' * (number - (len(stars) * 2))}"
        f"{stars}" for stars in star_generator
    ]