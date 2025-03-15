import re

txt = input("Enter sentence: ")
x = re.sub(r"([a-z])([A-Z])",r"\1_\2",txt).lower()
if x:
    print(x)
else:
    print("No match")