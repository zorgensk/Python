# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.

number = int(input("Введите число: "))
result = 0

for i  in range(number):
    i += 1
    i = (1 + 1/i)**i
    result += i

print(round(result, 3))