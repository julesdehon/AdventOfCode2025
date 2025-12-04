from pathlib import Path


def is_invalid_1(n: int) -> bool:
    pattern = str(n)
    return pattern[: len(pattern) // 2] == pattern[len(pattern) // 2 :]


def is_invalid_2(n: int) -> bool:
    pattern = str(n)
    divisors = [i for i in range(1, len(pattern)) if len(pattern) % i == 0]
    for divisor in divisors:
        chunks = [
            pattern[i * divisor : (i + 1) * divisor]
            for i in range(0, len(pattern) // divisor)
        ]
        if len(set(chunks)) == 1:
            return True

    return False


def main() -> None:
    input_lines = Path("input/input.txt").read_text("utf-8").strip().split("\n")
    ranges = [
        [int(n) for n in raw_range.split("-")]
        for raw_range in input_lines[0].split(",")
    ]

    result_1 = 0
    result_2 = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_1(n):
                result_1 += n
            if is_invalid_2(n):
                result_2 += n

    print(result_1)
    print(result_2)


if __name__ == "__main__":
    main()
