from typing import Iterator
from second_december.utils.utils import read_data


DIRECTION_CHECKS = {
    "ASC": lambda x, y: x < y,
    "DESC": lambda x, y: x > y,
}


def is_levels_distance_safe(x: int, y: int, direction: str) -> bool:
    return x != y and DIRECTION_CHECKS[direction](x, y) and 1 <= abs(x - y) <= 3


def check_tolerance(report: list[int], idx) -> bool:
    return (
        is_report_safe(iter(report[:idx] + report[idx + 1 :]), tolerate=False)
        or is_report_safe(iter(report[: idx + 1] + report[idx + 2 :]), tolerate=False)
        or is_report_safe(iter(report[: idx - 1] + report[idx:]), tolerate=False)
    )


def is_report_safe(report: Iterator[int], tolerate: bool) -> bool:
    backup_report = list(report)
    print(backup_report)
    report = iter(backup_report)

    first = next(report, None)
    second = next(report, None)
    if first is None or second is None:
        return False

    direction = "ASC"
    if first > second:
        direction = "DESC"

    iterated_levels = [first, second]
    is_safe = is_levels_distance_safe(first, second, direction)
    if not is_safe and tolerate:
        return check_tolerance(backup_report, 1)

    while is_safe and (y := next(report, None)) is not None:
        is_safe = is_levels_distance_safe(iterated_levels[-1], y, direction)
        if not is_safe and tolerate:
            return check_tolerance(backup_report, len(iterated_levels) - 1)
        iterated_levels.append(y)

    return is_safe


def get_safe_reports(reports: list[list[int]]) -> int:
    safe_counter = 0
    for report in reports:
        safe_counter += int(is_report_safe(iter(report), tolerate=False))

    return safe_counter


def get_almost_safe_reports(reports: list[list[int]]) -> int:
    safe_counter = 0
    for report in reports:
        safe_counter += int(is_report_safe(iter(report), tolerate=True))

    return safe_counter


if __name__ == "__main__":
    print("Safe reports are: ", get_safe_reports(read_data()))
    print("Almost safe reports are: ", get_almost_safe_reports(read_data()))
