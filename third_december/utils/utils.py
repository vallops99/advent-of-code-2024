def read_data() -> str:
    file = open("./third_december/data/data.txt", "r")
    return "".join(file.readlines())
