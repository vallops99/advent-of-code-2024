from first_december.utils.utils import read_data


def get_distance(left: list[int], right: list[int]):
    left.sort()
    right.sort()

    total_distance = 0
    for idx, number in enumerate(left):
        total_distance += abs(number - right[idx])

    return total_distance


if __name__ == "__main__":
    print("total distance is: ", get_distance(*read_data()))
