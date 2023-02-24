# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите натуральное число: "))

i = 2
primeFactor = []
while number != 1:
     if number % i == 0:
        number /= i
        primeFactor.append(i)
     else:
        i +=1

print(primeFactor)