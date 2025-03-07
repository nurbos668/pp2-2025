n = int(input())

gen = (x ** 2 for x in range(1, n+1))

for num in gen:
    print(num)