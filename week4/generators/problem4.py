n = int(input())

generator = (x for x in range(n, -1, -1))

print(*generator, sep=", ")