from itertools import combinations
coms = []
while True:
    lst = list(map(int,input().split()))
    
    if lst[0] == 0:
        break
    n = lst.pop(0)
    coms.append(list(combinations(lst, 6)))
    
for com in coms:
    for c in com:
        for i in c:
            print(i, end=' ')
        print()
    print()
        