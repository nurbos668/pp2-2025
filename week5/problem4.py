import re

txt = input("Enter sentence: ")
x = re.findall(r"\b[A-Z][a-z]+\b", txt)
if x:
    print(x)
else:
    print("No match")