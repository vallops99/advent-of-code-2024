import csv


def normalize_to_csv():
    file = open("./fifth_december/data/data.txt", "r")
    rules: list[list[str]] = []
    data: list[list[str]] = []
    are_rules_done = False
    rows = file.readlines()
    file.close()
    for row in rows:
        if are_rules_done:
            data.append(list(map(lambda x: x.strip(), row.split(","))))
        else:
            if row == "\n":
                are_rules_done = True
                continue
            rules.append(list(map(lambda x: x.strip(), row.split("|"))))

    csv_file = open("./fifth_december/data/rules.csv", "w")
    csv_file.write("\n".join(map(lambda x: ",".join(x), rules)))
    csv_file.close()
    csv_file = open("./fifth_december/data/data.csv", "w")
    csv_file.write("\n".join(map(lambda x: ",".join(x), data)))
    csv_file.close()


def read_data() -> tuple[dict[str, list[int]], list[list[int]]]:
    return _read_rules(), _read_input()


def _read_rules() -> dict[str, list[int]]:
    file = open("./fifth_december/data/rules.csv", "r")
    csv_reader = csv.reader(file, delimiter=",")
    rules: dict[str, list[int]] = {}
    for row in csv_reader:
        if rules.get(row[0], None) is None:
            rules[row[0]] = [int(row[1])]
        else:
            rules[row[0]].append(int(row[1]))
    file.close()
    return rules


def _read_input() -> list[list[int]]:
    file = open("./fifth_december/data/data.csv", "r")
    csv_reader = list(csv.reader(file, delimiter=","))
    data = list(map(lambda x: list(map(lambda y: int(y), x)), csv_reader))
    file.close()
    return data
