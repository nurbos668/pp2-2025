import re

txt = input("Enter sentence: ")
x = re.sub(r"([a-z])([A-Z])", r"\1 \2" ,txt)
if x:
    print(x)
else:
    print("No match")