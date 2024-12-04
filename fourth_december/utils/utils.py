def get_data() -> list[str]:
    return list(
        map(
            lambda x: x.strip(),
            open("./fourth_december/data/data.txt", "r").readlines(),
        )
    )
