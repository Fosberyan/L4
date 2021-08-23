from itertools import count, cycle
from typing import Generator, List


def random(start: int, iterations: int = 10) -> Generator:
    for i in range(start, start + iterations):
        yield i


def cycled(input_list: List, iterations: int = 10) -> Generator:
    cycler = cycle(input_list)
    for _ in range(0, iterations):
        yield next(cycler)


print(list(random(7, 77)))
print(list(cycled([7, 77], 2)))

