# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

listInput = [2, 3, 4, 5, 6]
newList = []
rangeList = len(listInput) / 2 + 0.5
for i in range(int(len(listInput) / 2 + 0.5)): 
    
    newList.append(listInput[i] * listInput[-i - 1])
    
print(newList)
