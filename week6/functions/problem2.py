a = input("Enter string: ")
upper_count = 0
lower_count = 0
for i in a:
    if i.isalpha() == False:
        continue
    elif i == i.upper():
        upper_count+=1
    else:
        lower_count+=1

print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)