import re

text = open(file='file.txt')
scratch_cards = [[line.strip(),1,0] for line in text.readlines()]
text.close()
total = 0
def process_numsequence(line):
    nums = set()
    for iter in re.finditer('[0-9]+', line):
        nums.add(int(iter.group(0)))
    return nums


for line in scratch_cards[:]:
    left, right = line[0].split('|')
    left = left.split(':')[1]
    left = process_numsequence(left)
    right = process_numsequence(right)
    common = len(left.intersection(right))
    line[2] = common

summa = 0
for j in range(len(scratch_cards)):
    reward = scratch_cards[j][2]
    for k in range(reward):
        scratch_cards[j+k+1][1]+=scratch_cards[j][1]
    summa+= scratch_cards[j][1]

print(summa)