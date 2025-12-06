from dataclasses import dataclass
from pathlib import Path


@dataclass
class Range:
    min: int
    max: int

    def __contains__(self, item: int) -> bool:
        return self.min <= item <= self.max

    def __len__(self) -> int:
        return self.max + 1 - self.min

    def try_merge(self, other: "Range") -> bool:
        if self.min > other.max:
            return False

        if other.min > self.max:
            return False

        self.min = min(self.min, other.min)
        self.max = max(self.max, other.max)
        return True

    @staticmethod
    def from_str(s: str) -> "Range":
        a, b = s.split("-")
        return Range(int(a), int(b))


def merge_ranges(ranges: list[Range]) -> list[Range]:
    sorted_ranges = sorted(ranges, key=lambda r: r.min)
    merged_ranges: list[Range] = []
    for r in sorted_ranges:
        for new_r in merged_ranges:
            if new_r.try_merge(r):
                break
        else:
            merged_ranges.append(r)

    return merged_ranges


def main() -> None:
    raw_ranges, raw_ingredient_ids = (
        Path("input/input.txt").read_text("utf-8").strip().split("\n\n")
    )
    ranges = [Range.from_str(raw_range) for raw_range in raw_ranges.split("\n")]
    merged_ranges = merge_ranges(ranges)
    ingredient_ids = [
        int(ingredient_id) for ingredient_id in raw_ingredient_ids.split("\n")
    ]

    p1 = len(
        [
            ingredient_id
            for ingredient_id in ingredient_ids
            if any(ingredient_id in r for r in merged_ranges)
        ]
    )
    print(p1)

    p2 = sum(len(r) for r in merged_ranges)
    print(p2)


if __name__ == "__main__":
    main()
