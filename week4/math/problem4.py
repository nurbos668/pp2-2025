import math

def parallelogram_area(base, height):
    return base * height


base = float(input("Введите длину основания: "))
height = float(input("Введите высоту: "))

area = parallelogram_area(base, height)
print("Площадь параллелограмма:", area)
