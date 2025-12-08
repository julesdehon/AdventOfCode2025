from copy import deepcopy
from pathlib import Path


def part1(original_grid: list[list[str]]) -> int:
    grid = deepcopy(original_grid)
    num_splits = 0
    for y, line in enumerate(grid[1:]):
        for x, c in enumerate(line):
            if c == "." and grid[y - 1][x] in ("S", "|"):
                grid[y][x] = "|"
            elif c == "^" and grid[y - 1][x] in ("S", "|"):
                num_splits += 1
                grid[y][x - 1] = "|"
                grid[y][x + 1] = "|"

    return num_splits


def part2(original_grid: list[list[str]]) -> int:
    num_timelines = [
        [0 for _ in range(len(original_grid[0]))] for _ in range(len(original_grid))
    ]
    num_timelines[-1] = [1 for _ in range(len(original_grid[-1]))]

    for y, row in reversed(list(enumerate(original_grid[:-1]))):
        for x, c in enumerate(row):
            if c in (".", "S") and original_grid[y + 1][x] == ".":
                num_timelines[y][x] = num_timelines[y + 1][x]
            elif c in (".", "S") and original_grid[y + 1][x] == "^":
                num_timelines[y][x] = (
                    num_timelines[y + 1][x - 1] + num_timelines[y + 1][x + 1]
                )

    x_start = original_grid[0].index("S")
    return num_timelines[0][x_start]


def main() -> None:
    grid = [
        list(s) for s in Path("input/input.txt").read_text("utf-8").strip().split("\n")
    ]
    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()
