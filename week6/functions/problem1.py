a = input("Enter numbers: ")
numbers = list(map(int,a.split()))
sum = 1
for i in numbers:
    sum *= i

print(sum)