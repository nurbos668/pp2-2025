import re

txt = input()

x = re.findall("[a-z]+_+[a-z]+", txt)

if x:
    print(x)
else:
    print("No match")