thisset = {"apple", "banana", "cherry"}
print(thisset)


# to add something to set we use method 'add'
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# The object in the update() doesnt must be necessarily set, it can be any(list, tuple, dict etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.


# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


# To unite 3 or more sets you can use the "union" method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)