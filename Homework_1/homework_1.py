'''1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет


weekday = int(input('Введите порядковый номер дня недели: '))

def weeknumber(n):
    if 0 < n < 6:
        print('Будний день')
    elif 5 < n < 8:
        print('Выходной день')
    else:
        print('Неверный номер дня!')

weeknumber(weekday)
'''

'''2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
*Пример:*
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

a = int(input('Ведите координату X: '))
b = int(input('Ведите координату Y: '))

def FindQvart(x, y):
    if(x > 0 and y > 0):
        print('Точка размещена в четверти 1')
    elif(x < 0 and y > 0):
        print('Точка размещена в четверти 2')
    elif(x < 0 and y < 0):
        print('Точка размещена в четверти 3')
    elif(x > 0 and y < 0):
        print('Точка размещена в четверти 4')
    else:
        if(x == 0 and y != 0):
            print('Точка размещена на оси Y')
        elif(x != 0 and y == 0):
            print('Точка размещена на оси X')
        else:
            print('Точка размещена на пересечении осей координат')

FindQvart(a, b)

