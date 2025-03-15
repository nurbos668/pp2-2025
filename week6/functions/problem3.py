a = input("Enter string:")
rev = ''.join(reversed(a))
if rev == a:
    print("Palindrome")
else:
    print("Not Palindrome")

print(rev)
print(a)