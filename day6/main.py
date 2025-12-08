import operator
from functools import reduce
from itertools import groupby
from pathlib import Path
from typing import Callable


def parse(raw_operator: str) -> Callable[[int, int], int]:
    return {"+": operator.add, "*": operator.mul}[raw_operator]


def main() -> None:
    input_lines = Path("input/input.txt").read_text("utf-8").strip().split("\n")
    rows = [[int(raw_n) for raw_n in line.split()] for line in input_lines[:-1]]
    columns = [
        "".join([row[i] for row in input_lines[:-1]])
        for i in range(len(input_lines[0]))
    ]
    column_groups = [
        list(int(x) for x in group)
        for key, group in groupby(columns, key=lambda x: x.strip() != "")
        if key
    ]
    operators = [parse(op) for op in input_lines[-1].split()]

    grand_total_p1 = 0
    grand_total_p2 = 0
    for i, op in enumerate(operators):
        ns = [row[i] for row in rows]
        grand_total_p1 += reduce(op, ns)
        grand_total_p2 += reduce(op, column_groups[i])

    print(grand_total_p1)
    print(grand_total_p2)


if __name__ == "__main__":
    main()
