import math

AD = float(input("Введите размер нижнего основания трапеции "))
BC = float(input("Введите размер верхнего основания трапеции "))
BK = float(input("Введите размер высоты "))
AK = (AD - BC)/2
AB = math.sqrt(AK**2 + BK**2)
Per = 2*AB + BC + AD
print("Периметр трапеции = ", Per)
