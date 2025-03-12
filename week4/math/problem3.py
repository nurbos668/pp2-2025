import math

def regular_polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))


n = int(input("Введите количество сторон: "))
s = float(input("Введите длину стороны: "))

area = regular_polygon_area(n, s)
print("Площадь правильного многоугольника:", area)
