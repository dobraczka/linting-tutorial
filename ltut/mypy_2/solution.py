from typing import Iterable

def get_divisible_by_two(values: Iterable[float]) -> list[float]:
    return [x for x in values if x % 2 == 0]
