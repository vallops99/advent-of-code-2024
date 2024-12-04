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


def is_MAS(rows: list[str], idx: int, subidx: int) -> bool:
    return (
        rows[idx][subidx] == "A"
        and len(rows) - 1 > idx > 0
        and len(rows[idx]) - 1 > subidx > 0
        and (
            (
                rows[idx - 1][subidx - 1] == "M"
                and rows[idx - 1][subidx + 1] == "M"
                and rows[idx + 1][subidx + 1] == "S"
                and rows[idx + 1][subidx - 1] == "S"
            )
            or (
                rows[idx - 1][subidx - 1] == "S"
                and rows[idx - 1][subidx + 1] == "S"
                and rows[idx + 1][subidx + 1] == "M"
                and rows[idx + 1][subidx - 1] == "M"
            )
            or (
                rows[idx - 1][subidx - 1] == "M"
                and rows[idx - 1][subidx + 1] == "S"
                and rows[idx + 1][subidx + 1] == "S"
                and rows[idx + 1][subidx - 1] == "M"
            )
            or (
                rows[idx - 1][subidx - 1] == "S"
                and rows[idx - 1][subidx + 1] == "M"
                and rows[idx + 1][subidx + 1] == "M"
                and rows[idx + 1][subidx - 1] == "S"
            )
        )
    )


def get_all_mas_x_shaped(rows: list[str]) -> int:
    mas_x_shaped_counter = 0
    for idx, row in enumerate(rows):
        for subidx in range(0, len(row)):
            mas_x_shaped_counter += is_MAS(rows, idx, subidx)

    return mas_x_shaped_counter


if __name__ == "__main__":
    print("All XMAS are: ", get_all_xmas(get_data()))
    print("All MAS X shape: ", get_all_mas_x_shaped(get_data()))
