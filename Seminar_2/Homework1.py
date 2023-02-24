# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите число: ")
temp = 0
res = 0

x = len(number)
number = float(number) * 10**x

while number > 0:
   temp =  number % 10
   res += temp
   number = number // 10

print(f'Cумма чисел = {int(res)}')
