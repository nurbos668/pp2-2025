lst = [1, 2, 3, 4]

f = open("text", "a")

for num in lst:
    f.write(str(num))
