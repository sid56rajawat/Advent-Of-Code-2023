import sys
D = open(sys.argv[1]).read().strip()
ans = 0
constraints = {"red": 12, "green": 13, "blue": 14}

def possibleSet(set):
    allPossibleCubes = True
    for cubes in set.split(','):
        colorCube = cubes.strip().split(' ')
        if(int(colorCube[0]) > constraints[colorCube[1]]):
            allPossibleCubes = False
            break
    return allPossibleCubes

for line in D.split('\n'):
    gameId = line[5:line.find(':')]
    game = line[line.find(':')+2:]
    allPossibleSets = True
    for set in game.split(';'):
        if(possibleSet(set) != True):
            allPossibleSets = False
            break
    if(allPossibleSets): ans += int(gameId)
print(ans)
