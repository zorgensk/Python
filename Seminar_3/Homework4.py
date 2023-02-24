# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dexNumber = int(input("Введите число: "))
binNumber = []
ostatok = None

while dexNumber != 0:
    ostatok = dexNumber % 2
    binNumber.append(ostatok)
    dexNumber = dexNumber // 2
print(binNumber[: : -1])