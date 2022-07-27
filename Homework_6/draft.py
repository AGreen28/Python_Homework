import re

primer = input('Введите математическое выражение: ')
#primer = '2+11*5-8/4+18'
nums = re.split('\+|\-|\/|\*', primer)
nums = list(map(float, nums))

oper = []
for i in primer:
    if i.isdigit() == False:
        oper.append(i)

def actions(a,x,y):
    if a == '*':
        res = x*y
    elif a == '/':
        res = x/y
    elif a == '+':
        res = x+y
    else:
        res = x-y
    return res

def main(oper, nums):
    inoper = []
    for i in range(len(oper)):
        inoper.append(i)
    oper_dict = dict(zip(inoper, oper))
    def poryadok(smbl1, smbl2):
        por = [k for k, v in oper_dict.items() if v == smbl1 or v == smbl2]
        return por
    prior = []
    prior.append(poryadok('*', '/'))
    prior.append(poryadok('+', '-'))
    prior = [x for l in prior for x in l]
    n = prior[0]
    nums[n] = actions(oper[n], nums[n], nums[n+1])
    del nums[n+1]
    del oper[n]
    return nums, oper

while len(nums) > 1:
    main(oper, nums)

print('Ответ: ', nums[0])