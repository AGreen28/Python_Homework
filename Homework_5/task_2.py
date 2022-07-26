'''Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7] => [1, 5]
'''

arr = [1, 5, 2, 3, 4, 6, 1, 7]
#arr = [1, 5, 2, 3, 4, 1, 7]

def increase(array):
    ar2 = min(array)
    for i in range(len(array)):
        for i in range(len(array)):
            if array[i] == (ar2 + 1):
                ar2 = array[i]
    newarr = [min(array), ar2]
    return newarr

print(increase(arr))