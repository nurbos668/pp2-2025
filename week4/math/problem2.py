def area(x1, x2, h):
    return (x1 + x2) * h / 2

f_value, s_value, height = float(input()), float(input()), float(input())

print(area(f_value, s_value, height))