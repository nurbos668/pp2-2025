def Squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


for num in Squares(int(input()), int(input())):
    print(num)