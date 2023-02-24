# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите натуральную степень многочлена k:'))

koeff=[randint(0,100) for i in range(k)]+[randint(1,100)]
res =' + '.join ([f'{j}x^{i}' for i, j in enumerate(koeff)][::-1])
res = res.replace('x^1', 'x')
res = res.replace('x^0', '')

print(f'{res} = 0')
