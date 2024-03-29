with open('polinom1.txt') as p1:
    print(*p1)
with open('polinom2.txt') as p2:
    print(*p2)

with open('polinom1.txt') as p1:
    p1 = p1.read().split(' + ')
with open('polinom2.txt') as p2:
    p2 = p2.read().split(' + ')

def outx(pol):
    pol2 = []
    for i in pol:
        pol2.append(i.split('*'))
    pol2 = [tuple(x) for x in pol2]
    return pol2

p11 = outx(p1)
p22 = outx(p2)

def sp_to_dict(pol):
    pol_dict = {}
    for x in pol:
        pol_dict[x[0]] = x[1:]
    inverse_pol_dict = dict(zip(pol_dict.values(), pol_dict.keys()))
    return inverse_pol_dict

p11_dict = sp_to_dict(p11)
p22_dict = sp_to_dict(p22)

def mergeDict(dict1, dict2):
    for k, v in dict2.items():
        if dict1.get(k):
            dict1[k] = [dict1[k], v]
        else:
            dict1[k] = v        
    return dict1

p_dict = mergeDict(p11_dict, p22_dict)

p33 = list(p_dict.items())

p33 = list(map(list, p33))

for i in range(0, len(p33)):
    for j in range(0, len(p33[i])):
        p33[i][j] = str(p33[i][j])

for i in range(0, len(p33)):
    for j in range(0, len(p33[i])):
        p33[i][j] = p33[i][j].replace('(', '')
        p33[i][j] = p33[i][j].replace(')', '')
        p33[i][j] = p33[i][j].replace(',', '')
        p33[i][j] = p33[i][j].replace("'", '')
        p33[i][j] = p33[i][j].replace("[", '')
        p33[i][j] = p33[i][j].replace("]", '')

for i in range(0, len(p33)):
    p33[i].reverse()
    for j in range(0, len(p33[i])):
        if j % 2 ==0:
            if p33[i][j].isdigit():
                p33[i][j] = int(p33[i][j])
                p33[i][j] = str(p33[i][j])
            else:
                st = p33[i][j]
                st = st.split()
                p33[i][j] = int(st[0]) + int(st[1])
                p33[i][j] = str(p33[i][j])

for i in range(0, len(p33)-1):
    for j in range(0, len(p33[i])-1):
        p33[i][0] = p33[i][0] + '*'

for i in range(0, len(p33)):
    for j in range(0, len(p33[i])):
        p33[i] = ''.join(p33[i])

p33 = ' + '.join(map(str, p33))
print(p33)

sumfile = open("sumofpolinoms.txt", "w")
sumfile.write(p33)
sumfile.close()