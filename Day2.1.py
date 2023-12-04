import re

idsum = 0
for i in range(1,101):
    text = input().split(';')
    text[0] = text[0].split(':')[1]
    isntFine = False
    for game in text:
        balls = game.split(',')
        thisGame = {}
        for colour in balls:
            thisGame[colour.split(' ')[-1]]= int(re.findall('[0-9]+', colour)[0])
        if 'blue' in thisGame.keys():
            isntFine = True if thisGame['blue']>14 else isntFine
        if 'red' in thisGame.keys():
            isntFine = True if thisGame['red']>12 else isntFine
        if 'green' in thisGame.keys():
            isntFine = True if thisGame['green']>13 else isntFine
    idsum = idsum + i if not isntFine else idsum
print(idsum)