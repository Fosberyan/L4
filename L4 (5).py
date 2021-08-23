from functools import reduce
a = range(100, 1001, 2)
b = reduce(lambda a, b: int(a) * int(b), a)
print(f'Итог: {b}')