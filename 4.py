import sys
table = open(sys.argv[1]).read().strip()

cards = table.split('\n')
matchingNumbersCount = [0] * len(cards)
for i in range(0,len(cards)):
    card = cards[i]
    wn, on = card.split('|')
    wn = wn.split(':')[1]
    winningNumbers = set(wn.split(' '))
    winningNumbers.remove('')
    ourNumbers = on.split(' ')
    cnt = 0
    for num in ourNumbers:
        if(num in winningNumbers): cnt+=1
    matchingNumbersCount[i] += cnt

instances = [1] * len(cards)
for i in range(0,len(cards)):
    mnc = matchingNumbersCount[i]
    for j in range(1,mnc+1):
        if(i+j < len(cards)): instances[i+j] += instances[i]

print(sum(instances))
