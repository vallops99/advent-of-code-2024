import csv


def normalize_to_csv():
    file = open("./second_december/data/data.txt", "r")
    numbers: list[list[str]] = []
    for line in file.readlines():
        splitted_line = line.split(" ")
        numbers.append(list(map(lambda x: x.lstrip(), splitted_line)))

    file.close()
    csv = open("./second_december/data/data.csv", "w+")

    for number_pair in numbers:
        csv.write(",".join(number_pair))
    csv.close()


def read_data() -> list[list[int]]:
    file = open("./second_december/data/data.csv", "r")
    csv_reader = csv.reader(file, delimiter=",")
    levels = []
    for row in csv_reader:
        levels.append(list(map(int, row)))

    return levels


def check_result():
    result_file = open("./second_december/result/result.csv")
    result = result_file.readlines()
    result_file.close()

    brute_file = open("./second_december/result/brute_result.csv")
    brute_result = brute_file.readlines()
    brute_file.close()
    for idx, res in enumerate(result):
        if res != brute_result[idx]:
            print(idx + 1)
