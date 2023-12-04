import re

allmight = 0
for i in range(1,101):
    text = input().split(';')
    text[0] = text[0].split(':')[1]
    currentMaxes = {'blue':0, 'red':0, 'green':0}
    for game in text:
        balls = game.split(',')
        thisGame = {}
        for colour in balls:
            thisGame[colour.split(' ')[-1]]= int(re.findall('[0-9]+', colour)[0])
        if 'blue' in thisGame.keys():
            currentMaxes['blue'] = max(currentMaxes['blue'], thisGame['blue'])
        if 'red' in thisGame.keys():
            currentMaxes['red'] = max(currentMaxes['red'], thisGame['red'])
        if 'green' in thisGame.keys():
            currentMaxes['green'] = max(currentMaxes['green'], thisGame['green'])
    power = currentMaxes['blue']*currentMaxes['red']*currentMaxes['green']
    allmight+=power
print(allmight)