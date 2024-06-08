import sys
D = open(sys.argv[1]).read().strip()
totalPower = 0

def findPower(game):
    minCubes = {"red": 0, "blue": 0, "green": 0}
    for set in game.split(';'):
        for colorCubes in set.split(','):
            colorCube = colorCubes.strip().split(' ')
            count, color = int(colorCube[0]), colorCube[1]
            if(minCubes[color] < count): minCubes[color] = count
    return minCubes['red'] * minCubes['blue'] * minCubes['green']

for line in D.split('\n'):
    game = line[line.find(':')+2:]
    totalPower += findPower(game)
print(totalPower)
