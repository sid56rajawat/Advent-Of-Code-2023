import sys
file = open(sys.argv[1]).read().strip().split('\n\n')

seeds = [int(i) for i in file[0].split(' ')[1:]]
file = file[1:]

maps = dict()
mapKeys = []
for line in file:
    lineParts = line.split('\n')
    key = lineParts[0][:-5]
    val = []
    for mapRange in lineParts[1:]:
        val.append([int(i) for i in mapRange.split(' ')])
    maps[key] = val
    mapKeys.append(key)


minLocation = 2 ** 31
for seed in seeds:
    materialVal = seed
    for key in mapKeys:
        # print(key)
        map = maps[key]
        for ranges in map:
            if(ranges[1] <= materialVal <= ranges[1] + ranges[2]):
                # print("using",key,ranges)
                materialVal += (ranges[0] - ranges[1])
                # print(materialVal)
                break
    if(materialVal < minLocation):
        minLocation = materialVal

print(minLocation)