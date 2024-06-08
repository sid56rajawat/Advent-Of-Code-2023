import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

def hasSymbol(i, j, matrix):
    rows, cols = len(matrix), len(matrix[0])
    # top
    if(i-1 >= 0 and matrix[i-1][j] != '.' and (not matrix[i-1][j].isnumeric())):
        return True
    # top-right
    if(i-1 >= 0 and j+1 < cols and matrix[i-1][j+1] != '.' and (not matrix[i-1][j+1].isnumeric())):
        return True
    # right
    if(j+1 < cols and matrix[i][j+1] != '.' and (not matrix[i][j+1].isnumeric())):
        return True
    # down-right
    if(i+1 < rows and j+1 < cols and matrix[i+1][j+1] != '.' and (not matrix[i+1][j+1].isnumeric())):
        return True
    # down
    if(i+1 < rows and matrix[i+1][j] != '.' and (not matrix[i+1][j].isnumeric())):
        return True
    # down-left
    if(i+1 < rows and j-1 >= 0 and matrix[i+1][j-1] != '.' and (not matrix[i+1][j-1].isnumeric())):
        return True
    # left
    if(j-1 >= 0 and matrix[i][j-1] != '.' and (not matrix[i][j-1].isnumeric())):
        return True
    # top-left
    if(i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] != '.' and (not matrix[i-1][j-1].isnumeric())):
        return True
    return False

ans = 0
for i in range(0,len(lines)):
    line = lines[i]
    # go from left
    # if . continue
    # else add to builder and check neighbors if sym -> flag = true
    #      when . or EOL -> if flag add to total
    isBuilding = False
    nearSymbol = False
    building = ''
    for j in range(0,len(line)+1):
        if(isBuilding):
            if(j == len(line) or not(line[j].isnumeric())):
                if(nearSymbol):
                    ans += int(building)
                building = ''
                nearSymbol = False
                isBuilding = False
            elif(line[j].isnumeric()):
                building += line[j]
                nearSymbol = nearSymbol or hasSymbol(i,j,lines)

        else:
            if(j == len(line)): break
            if(line[j].isnumeric()):
                isBuilding = True
                building = line[j]
                nearSymbol = hasSymbol(i,j,lines)

print(ans)