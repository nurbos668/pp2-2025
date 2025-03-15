import re

txt = input("Enter sentence: ")
x = re.sub("_([a-z])", lambda match: match.group(1).upper(),txt)
if x:
    print(x)
else:
    print("No match")