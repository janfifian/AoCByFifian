import re
standard_symbols = {'0','1','2','3','4','5','6','7','8','9','.'}
text = open(file='file.txt')
data_array = [line.strip() for line in text.readlines()]
K = len(data_array)
total = 0

def verifyText(total, value, begin, end, p):
    for q in range(begin, end):
        if data_array[p][q] not in standard_symbols:
            total += value
            return (total, True)
    return (total, False)

for i in range(K):
    for iter in re.finditer('[0-9]+', data_array[i]):
        value =int(iter.group(0))
        begin = max(iter.span()[0]-1, 0)
        end = min(iter.span()[1]+1, len(data_array[i])-1)
        vrangeBegin = max(i-1, 0)
        vrangeEnd = min(i+2, K)


        for p in range(vrangeBegin,vrangeEnd):
            total, changed = verifyText(total,value,begin,end,p)
            if(changed):
                break

print(total)