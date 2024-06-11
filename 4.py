import sys
table = open(sys.argv[1]).read().strip()

# for each card
# make set of Winning numbers
# then iterate through our numbers and increment count
# if our number in winning numbers
# at the end: ans += cnt == 0 ? 0 : 2 ** (cnt-1)
ans = 0
for card in table.split('\n'):
    wn, on = card.split('|')
    wn = wn.split(':')[1]
    winningNumbers = set(wn.split(' '))
    winningNumbers.remove('')
    ourNumbers = on.split(' ')
    cnt = 0
    for num in ourNumbers:
        if(num in winningNumbers): cnt+=1
    ans += 0 if cnt == 0 else 2 ** (cnt-1)
    
print(ans)