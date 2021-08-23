from random import randint

spicok = [randint(-14, 88) for _ in range(33)]
itog = [el for el in spicok if spicok.count(el) == 1]
print(f'Старт\n{spicok}\nФиниш\n{itog}')


