import re
from third_december.utils.utils import read_data


def find_all_matches(data: str, with_action: bool) -> list[str]:
    regexes = [r"mul\(\d{1,3},\d{1,3}\)", r"mul\(\d{1,3},\d{1,3}\)|don't|do"]
    return re.findall(regexes[int(with_action)], data)


def get_multiplication_value(data: str) -> int:
    sum_of_mul = 0
    for mul in find_all_matches(data, False):
        values = mul[4:].split(",")
        sum_of_mul += int(values[0]) * int(values[1][:-1])

    return sum_of_mul


def get_multiplication_value_by_action(data: str) -> int:
    sum_of_mul = 0
    last_instruction = "do"
    for instruction in find_all_matches(data, True):
        if instruction == "don't" or instruction == "do":
            last_instruction = instruction
            continue
        if last_instruction == "don't":
            continue

        values = instruction[4:].split(",")
        sum_of_mul += int(values[0]) * int(values[1][:-1])

    return sum_of_mul


if __name__ == "__main__":
    print("Sum of mul is: ", get_multiplication_value(read_data()))
    print("Sum of mul by action is: ", get_multiplication_value_by_action(read_data()))
