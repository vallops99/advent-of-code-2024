import re
from fourth_december.utils.utils import get_data


def get_all_xmas(rows: list[str]) -> int:
    xmas_counter = 0
    for idx, row in enumerate(rows):
        # Horizontal
        xmas_counter += len(re.findall(r"XMAS", row))
        xmas_counter += len(re.findall(r"SAMX", row))
        for subidx, char in enumerate(row):
            # Vertical
            if idx + 3 < len(rows):
                vertical = (
                    char
                    + rows[idx + 1][subidx]
                    + rows[idx + 2][subidx]
                    + rows[idx + 3][subidx]
                )
                xmas_counter += "XMAS" == vertical or "SAMX" == vertical
                # Diagonal right
                if subidx + 3 < len(row):
                    diagonal = (
                        char
                        + rows[idx + 1][subidx + 1]
                        + rows[idx + 2][subidx + 2]
                        + rows[idx + 3][subidx + 3]
                    )
                    xmas_counter += "XMAS" == diagonal or "SAMX" == diagonal
                # Diagonal left
                if subidx - 3 >= 0:
                    diagonal = (
                        char
                        + rows[idx + 1][subidx - 1]
                        + rows[idx + 2][subidx - 2]
                        + rows[idx + 3][subidx - 3]
                    )
                    xmas_counter += "XMAS" == diagonal or "SAMX" == diagonal

    return xmas_counter


if __name__ == "__main__":
    # print(get_data())
    print("All XMAS are: ", get_all_xmas(get_data()))
