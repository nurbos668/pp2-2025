import re

txt = input("Enter sentence: ")
x = re.split("[A-Z]",txt)
if x:
    print(x)
else:
    print("No match")