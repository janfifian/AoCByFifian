import re

sum = 0
tau = int(input())
for i in range(tau):
    txt = input()
    table = re.findall('[0-9]', txt)
    sum += 10*int(table[0])+int(table[-1])

print(sum)

