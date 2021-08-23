Lost = [0, 4, 8, 15, 16, 23, 42, 41, 40, 1]
Okeanic = [Lost[num] for num in range(1, len(Lost)) if Lost[num] > Lost[num - 1]]
print(Okeanic)