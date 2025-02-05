import problem1  # Убеждаемся, что файл problem1.py существует

print("Hi! I'm David, and I can help you with conversions. Enter grams:")
grams = float(input())  # Получаем число от пользователя

print("Great! Wait a second...")
print(f"{grams} grams is {problem1.to_ounces(grams):.2f} ounces.")
