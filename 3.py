import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

def findGearsNearMe(i, j, gearsNearMe):
    rows, cols = len(lines), len(lines[0])
    
    # Check all eight directions
    directions = [
        (-1, 0),  # top
        (1, 0),   # bottom
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # top-left
        (-1, 1),  # top-right
        (1, -1),  # bottom-left
        (1, 1)    # bottom-right
    ]
    
    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < rows and 0 <= new_j < cols and lines[new_i][new_j] == '*':
            gearsNearMe.add(str(new_i) + 'i' + str(new_j) + 'j')

potentialGears = {}
for i in range(0,len(lines)):
    line = lines[i]
    isBuilding = False
    building = ''
    gearsNearMe = set()
    for j in range(0,len(line)+1):
        if(isBuilding):
            if(j == len(line) or not(line[j].isnumeric())):
                # print(building,"->",gearsNearMe)
                for gear in gearsNearMe:
                    potentialGears.setdefault(gear, []).append(int(building))
                building = ''
                isBuilding = False
                gearsNearMe = set()
            elif(line[j].isnumeric()):
                building += line[j]
                findGearsNearMe(i,j,gearsNearMe)

        else:
            if(j == len(line)): break
            if(line[j].isnumeric()):
                isBuilding = True
                building = line[j]
                findGearsNearMe(i,j,gearsNearMe)

# print(potentialGears)
ans = 0
for gear in potentialGears:
    arr = potentialGears[gear]
    if(len(arr) == 2): ans += arr[0] * arr[1]
print(ans)