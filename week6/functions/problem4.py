import time
import math

def square_root_after_time (number,millsec):
    x = math.sqrt(number)
    time.sleep(millsec/1000)
    print(f"The square root of {int(number)} after {int(millsec)} milliseconds is {x}")

number = float(input("Enter number: "))
millsec = float(input("Enter specific milliseconds: "))
square_root_after_time(number,millsec)