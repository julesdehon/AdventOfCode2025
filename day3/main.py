from pathlib import Path


def get_max_joltage(line: str, n_digits: int) -> int:
    max_joltage = 0
    start = 0
    for n in reversed(range(n_digits)):
        (i, d) = max(
            enumerate([int(c) for c in line[start : len(line) - n]]), key=lambda x: x[1]
        )
        start += i + 1
        max_joltage += d * 10**n

    return max_joltage


def main() -> None:
    input_lines = Path("input/input.txt").read_text("utf-8").strip().split("\n")

    output_joltage_p1 = 0
    output_joltage_p2 = 0
    for line in input_lines:
        max_joltage_p1 = get_max_joltage(line, 2)
        max_joltage_p2 = get_max_joltage(line, 12)
        output_joltage_p1 += max_joltage_p1
        output_joltage_p2 += max_joltage_p2

    print(output_joltage_p1)
    print(output_joltage_p2)


if __name__ == "__main__":
    main()
