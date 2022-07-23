'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''

n = int(input('Введите число: '))

def Multipliers(x):
    mul = []
    for i in range(2, x):
        if x % i == 0:
            mul.append(i)
    return mul

print(Multipliers(n))
