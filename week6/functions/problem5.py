a = input("Enter list of 1 or 0: ")
booleans = tuple(map(int,a.split()))
x = all(booleans)
if x == True:
    print("Yes, all true")
else:
    print("No, not all true")