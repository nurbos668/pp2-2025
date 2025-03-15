import re

txt = input("Enter sentence: ")
x = re.findall("a.*b$", txt)
if x:
    print(x)
else:
    print("No match")