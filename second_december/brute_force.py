from second_december.utils.utils import read_data
from second_december.get_safe_reports import is_levels_distance_safe


def is_row_safe(report: list[int], direction: str) -> bool:
    report_iter = iter(report)
    is_safe = True
    x = next(report_iter, None)
    if x is None:
        return False

    while is_safe and (y := next(report_iter, None)) is not None:
        is_safe = is_levels_distance_safe(x, y, direction)
        x = y

    return is_safe


def brute_force_method(reports: list[list[int]]) -> int:
    result = []
    safe_counter = 0
    for report in reports:
        if is_row_safe(report, "ASC") or is_row_safe(report, "DESC"):
            result.append("True")
            safe_counter += 1
            continue

        for idx in range(0, len(report)):
            if is_row_safe(report[:idx] + report[idx + 1 :], "ASC") or is_row_safe(
                report[:idx] + report[idx + 1 :], "DESC"
            ):
                safe_counter += 1
                break

    return safe_counter


if __name__ == "__main__":
    print("Almost safe reports are: ", brute_force_method(read_data()))
