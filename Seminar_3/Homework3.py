# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



listInput = [1.1, 1.2, 3.1, 5, 10.01]
newList = []
i = 0
temp = 0
for i in listInput:  
    temp = i - int(i)
    newList.append(temp)
   
if 0 in newList:
    newList.remove(0)
result = round((max(newList) - min(newList)),2)
print(result)