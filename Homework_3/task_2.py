'''Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
'''

spisok1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_string1 = "qwe"
spisok2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
find_string2 = "йцу"
spisok3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
find_string3 = "йцу"
spisok4 = ["123", "234", 123, "567"]
find_string4 = "123"
spisok5 = []
find_string5 = "123"

def Indexes(x, sp):
    ind = []
    count = 0
    for i in range(0, len(sp)):
        if sp[i] == x:
            ind.append(i)
            count += 1
    if count > 1:
        print(ind[1])
    else:
        print(-1)

Indexes(find_string1, spisok1)
Indexes(find_string2, spisok2)
Indexes(find_string3, spisok3)
Indexes(find_string4, spisok4)
Indexes(find_string5, spisok5)
