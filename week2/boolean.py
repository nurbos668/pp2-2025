# This expressions will return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))