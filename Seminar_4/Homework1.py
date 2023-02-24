# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


numberZnak = float(input("С какой точностью вывести число Пи? : "))
numberPi = 3
k = 0
znak = 1
while k <= 2000000:
    k += 2
    numberPi += (4 * znak / (k * (k + 1) * (k + 2)))
    znak *= -1
i = 0
while numberZnak < 10:
    numberZnak = numberZnak / 0.1
    i += 1
strPi = list(str(numberPi))
Pi = strPi[:i]
print(''.join(map(str,Pi)))
