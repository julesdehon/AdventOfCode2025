import operator
from pathlib import Path
from typing import Callable


def get_operator(direction: str) -> Callable[[int, int], int]:
    if direction == "R":
        return operator.add
    elif direction == "L":
        return operator.sub
    else:
        raise ValueError


def main() -> None:
    input_lines = Path("input/input.txt").read_text("utf-8").strip().split("\n")
    position = 50
    password_1 = 0
    password_2 = 0

    for line in input_lines:
        direction, angle = (line[0], int(line[1:]))
        operate = get_operator(direction)
        for _ in range(angle):
            position = operate(position, 1) % 100
            if position == 0:
                password_2 += 1

        if position == 0:
            password_1 += 1

    print(password_1)
    print(password_2)


if __name__ == "__main__":
    main()
