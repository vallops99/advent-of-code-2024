from fifth_december.utils.utils import read_data


def get_middle_page_sum(rules: dict[str, list[int]], rows: list[list[int]]) -> int:
    return sum(
        map(
            lambda x: rows[x][int((len(rows[x]) - 1) / 2)], _get_indexes(rules, rows)[0]
        )
    )


def get_middle_fixed_page_sum(
    rules: dict[str, list[int]], rows: list[list[int]]
) -> int:
    _, bad_indexes = _get_indexes(rules, rows)
    fixed_indexes: list[list[int]] = []
    for idx in bad_indexes:
        fixed_indexes.append([rows[idx][0]])
        for subidx in range(1, len(rows[1:idx])):
            rule: list[int] = rules.get(str(rows[idx][subidx]), [])
            index = next(
                filter(lambda x: fixed_indexes[-1][x] in rule, list(range(0, subidx))),
                None,
            )
            if index:
                fixed_indexes[-1].insert(index, rows[idx][subidx])
            else:
                fixed_indexes[-1].append(rows[idx][subidx])

    return int(
        sum(
            map(
                lambda x: fixed_indexes[x][int((len(rows[x]) - 1) / 2)],
                range(0, len(fixed_indexes)),
            )
        )
    )


def _get_indexes(
    rules: dict[str, list[int]], rows: list[list[int]]
) -> tuple[set[int], set[int]]:
    result_indexes: set[int] = set()
    bad_indexes: set[int] = set()
    for idx in range(0, len(rows)):
        for subidx in range(1, len(rows[idx])):
            rule: list[int] = rules.get(str(rows[idx][subidx]), [])
            if len(list(filter(lambda x: x in rule, rows[idx][:subidx]))) == 0:
                result_indexes.add(idx)
                continue
            result_indexes.discard(idx)
            bad_indexes.add(idx)
            break

    return result_indexes, bad_indexes


if __name__ == "__main__":
    rules, data = read_data()
    print("Middle page sum is: ", get_middle_page_sum(rules, data))
    print("Middle fixed page sum is: ", get_middle_fixed_page_sum(rules, data))
