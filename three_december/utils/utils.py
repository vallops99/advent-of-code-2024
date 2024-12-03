def read_data() -> str:
    file = open("./three_december/data/data.txt", "r")
    return "".join(file.readlines())
