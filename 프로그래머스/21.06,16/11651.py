t = int(input())
list = []
for i in range(t):
    x,y = map(int,input().split())
    list.append([x,y])
list.sort(key = lambda x: (x[1],x[0]))

for i in list:
    print(*i)