import datetime
import math

date1 = datetime.datetime(2024, 6, 23, 12, 13, 12)
date2 = datetime.datetime(2024, 6, 23, 12, 13, 58)
difference = date1 - date2

print(f"The difference is {difference.seconds} second")