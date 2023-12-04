import re

text = open(file='file.txt')
data_array = [line.strip() for line in text.readlines()]
text.close()
total = 0
def process_numsequence(line):
    nums = set()
    for iter in re.finditer('[0-9]+', line):
        nums.add(int(iter.group(0)))
    return nums


for line in data_array:
    left, right = line.split('|')
    left = left.split(':')[1]
    left = process_numsequence(left)
    right = process_numsequence(right)
    common = len(left.intersection(right))
    total+= 0 if common ==0 else 2**(common-1)

print(total)