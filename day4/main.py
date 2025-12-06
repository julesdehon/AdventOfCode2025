from pathlib import Path


def around(grid: list[str], x: int, y: int) -> list[tuple[int, int]]:
    surrounding_coords = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) == (0, 0):
                continue

            if not 0 <= x + dx < len(grid[0]):
                continue

            if not 0 <= y + dy < len(grid):
                continue

            surrounding_coords.append((x + dx, y + dy))

    return surrounding_coords


def is_accessible(grid: list[str], x: int, y: int) -> bool:
    surrounding_rolls = 0
    for xx, yy in around(grid, x, y):
        if grid[yy][xx] == "@":
            surrounding_rolls += 1

    return surrounding_rolls < 4


def clear(grid: list[str]) -> tuple[int, list[str]]:
    num_accessible_rolls = 0
    new_grid = []
    for y, row in enumerate(grid):
        new_row = ""
        for x, _ in enumerate(row):
            if row[x] == "@" and is_accessible(grid, x, y):
                num_accessible_rolls += 1
                new_row += "."
            else:
                new_row += row[x]

        new_grid.append(new_row)

    return num_accessible_rolls, new_grid


def main() -> None:
    grid = Path("input/input.txt").read_text("utf-8").strip().split("\n")

    p1, grid = clear(grid)
    num_removed = p1
    p2 = num_removed

    while num_removed != 0:
        num_removed, grid = clear(grid)
        p2 += num_removed

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
