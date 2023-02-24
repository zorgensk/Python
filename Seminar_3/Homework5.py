# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

numberInput = int(input("Введите число"))

def fibonacсiPlus():
    number_one = 0
    number_two = 1
    fibo_list = [0, 1]
    for i in range(1,numberInput):
        numbers_three = number_one + number_two
        number_one = number_two
        number_two = numbers_three
        fibo_list.append(numbers_three)
    return fibo_list
fibo_list = fibonacсiPlus()

def fibonacсiMinus():
    number_one = 0
    number_two = 1
    fibo_list2 = [1]
    for i in range(1,numberInput):
        numbers_three = (number_one - number_two) 
        number_one = number_two
        number_two = numbers_three
        fibo_list2.append(numbers_three)
    fibo_list2 = fibo_list2[::-1]
    return fibo_list2

fibonacci= fibonacсiMinus() + fibonacсiPlus()

print(fibonacci)

