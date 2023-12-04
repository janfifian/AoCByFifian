import re

convy = dict(one=1, two=2,three=3,four=4,five=5,six=6,seven=7,eight=8,nine=9)
def toint(x):
    if x in convy.keys():
        return convy[x]
    else:
        return int(x)

sum = 0
tau = int(input())
for i in range(tau):
    txt = input()
    for name, number in convy.items():
        txt = txt.replace(name, f'{name}{number}{name}')
    table = re.findall('[0-9]',txt)
    sum += 10*int(table[0])+int(table[-1])

print(sum)

