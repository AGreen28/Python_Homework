X='X'
O='0'
RAZMER_DOSKI=9
HODI=' '
NICHYA='Ничья'

def nachalo(vopros):
    otvet=None
    while otvet not in ('y','n'):
        otvet=input(vopros).lower()
    return otvet

def fishki():
    perviy_hod=nachalo("Хочешь сделать первый ход (y/n)?  ")
    if perviy_hod=='y':
        print('Ты играешь крестиками!')
        human=X
        comp=O
    else:
        print('Я играю крестиками!')
        human=O
        comp=X
    return comp, human
        
def hod_number(low,high):
    otvet=None
    while True:
        try:
            stroka = int(input("Введите номер строки (1-3): "))
            break
        except:
            print('Введите число от 1 до 3!')
    while True:
        try:
            stolb = int(input("Введите номер столбца (1-3): "))
            break
        except:
            print('Введите число от 1 до 3!')
    while otvet not in range(low,high):
        if stroka == 1 and stolb == 1:
            otvet = 0
        elif stroka == 1 and stolb == 2:
            otvet = 1
        elif stroka == 1 and stolb == 3:
            otvet = 2
        elif stroka == 2 and stolb == 1:
            otvet = 3
        elif stroka == 2 and stolb == 2:
            otvet = 4
        elif stroka == 2 and stolb == 3:
            otvet = 5
        elif stroka == 3 and stolb == 1:
            otvet = 6
        elif stroka == 3 and stolb == 2:
            otvet = 7
        elif stroka == 3 and stolb == 3:
            otvet = 8
        else: 
            break
    return otvet


def new_doska():
    doska=[]
    for i in range(RAZMER_DOSKI):
        doska.append(HODI)
    return doska

def pokaz_doski(doska):
    print('\n', doska[0], '|', doska[1], '|', doska [2])
    print('-----------')
    print('\n', doska[3], '|', doska[4], '|', doska [5])
    print('-----------')
    print('\n', doska[6], '|', doska[7], '|', doska [8], '\n')

def dostupnie_hodi(doska):
    dostupnie_hodi=[]
    for i in range(RAZMER_DOSKI):
        if doska[i]== HODI:
            dostupnie_hodi.append(i)
    return dostupnie_hodi

def winner(doska):
    VAR_POBED=((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))
    for i in VAR_POBED:
        if doska[i[0]]==doska[i[1]]==doska[i[2]]!=HODI:
            winner=doska[i[0]]
            return winner
        if HODI not in doska:
            return NICHYA
    return None

def human_hod(doska,human):
    dostupnie=dostupnie_hodi(doska)
    hod=None
    while hod not in dostupnie:
        hod=hod_number(0,RAZMER_DOSKI)
        if hod not in dostupnie:
            print('Такая клетка недоступна. Выбери другую.')
    return hod

def comp_hod(doska,comp,human):
    doska=doska[:]
    BEST_HODI=(4,0,2,6,8,1,3,5,7)
    print('Ход компьютера:')
    for i in dostupnie_hodi(doska):
        doska[i]=comp
        if winner(doska)==comp:
            return i
        doska[i]=HODI
    for j in dostupnie_hodi(doska):
        doska[j]=human
        if winner(doska)==human:
            return j
        doska[j]=HODI
    for k in dostupnie_hodi(doska):
        return k

def next_ochered(ochered):
    if ochered==X:
        return O
    else:
        return X

def pozdrav_pobeditela(pobeditel,comp,human):
    if pobeditel!=NICHYA:
        print('Собрана линия ', pobeditel)
    else:
        print(NICHYA)
    if pobeditel==comp:
        print('Компьютер выиграл!', '\n')
    elif pobeditel==human:
        print('Ты победил!', '\n')
    elif pobeditel==NICHYA:
        print()
def main():
    comp,human=fishki()
    ochered=X
    doska=new_doska()
    pokaz_doski(doska)
    while not winner(doska):
        if ochered==human:
            hod=human_hod(doska,human)
            doska[hod]=human
        else:
            hod=comp_hod(doska,comp,human)
            doska[hod]=comp
        pokaz_doski(doska)
        ochered=next_ochered(ochered)
    pobeditel=winner(doska)
    pozdrav_pobeditela(pobeditel,comp,human)
    povtor = input('Повторим? (y/n): ')
    if povtor == 'y':
        main()

main()