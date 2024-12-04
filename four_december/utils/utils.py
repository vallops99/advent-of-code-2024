def get_data() -> list[str]:
    return list(
        map(lambda x: x.strip(), open("./four_december/data/data.txt", "r").readlines())
    )
