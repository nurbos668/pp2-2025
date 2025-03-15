import re

txt = input("Enter sentence: ")
x = re.findall("ab{2,3}",txt)
print(x)