import re
standard_symbols = {'0','1','2','3','4','5','6','7','8','9','.'}
text = open(file='file.txt')
data_array = [line.strip() for line in text.readlines()]
K = len(data_array)
total = 0

def appendGears(value, begin, end, p, gears):
    for q in range(begin, end):
        if data_array[p][q]=='*':
            gears[(p,q)][0]+=1
            gears[(p,q)][1].append(value)

gears = dict()

for i in range(K):
    for j in range(len(data_array[i])):
        if data_array[i][j]=='*':
            gears[(i,j)] = [0,[]]

for i in range(K):
    for iter in re.finditer('[0-9]+', data_array[i]):
        value =int(iter.group(0))
        begin = max(iter.span()[0]-1, 0)
        end = min(iter.span()[1]+1, len(data_array[i])-1)
        vrangeBegin = max(i-1, 0)
        vrangeEnd = min(i+2, K)


        for p in range(vrangeBegin,vrangeEnd):
            appendGears(value,begin,end,p,gears)

totality= 0

for gear in gears.values():
    if gear[0]==2:
        totality+=gear[1][0]*gear[1][1]

print(totality)