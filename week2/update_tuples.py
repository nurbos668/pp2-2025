tuples = (1, 2, 3, 4, 5)
lst = list(tuples)

print(lst)

lst[0] = 100

tuples = tuple(lst)

print(tuples)


tuples2 = ("banana", "apple", "morkov")
tuples3 = ("orange",)
print(tuples2 + tuples3)