n = int(input())

generator = (x for x in range(n+1) if x % 2 == 0)

print(*generator, sep=", ")