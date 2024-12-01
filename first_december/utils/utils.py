import csv


def normalize_to_csv():
    file = open("./first_december/data/data.txt", "r")
    numbers: list[list[str]] = []
    for line in file.readlines():
        splitted_line = line.split("  ")
        numbers.append(list(map(lambda x: x.lstrip(), splitted_line)))

    file.close()
    csv = open("./first_december/data/data.csv", "w+")

    for number_pair in numbers:
        csv.write(",".join(number_pair))
    csv.close()


def read_data() -> tuple[list[int], list[int]]:
    file = open("./first_december/data/data.csv", "r")
    csv_reader = csv.reader(file, delimiter=",")
    left = []
    right = []
    for row in csv_reader:
        left.append(int(row[0]))
        right.append(int(row[1]))

    return left, right
