from first_december.utils.utils import read_data


def get_similarity_score(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()

    similarity_score = 0
    for left_int in left:
        for right_int in right:
            if left_int < right_int:
                break
            if left_int == right_int:
                similarity_score += left_int

    return similarity_score


if __name__ == "__main__":
    print("Similarity score is: ", get_similarity_score(*read_data()))
