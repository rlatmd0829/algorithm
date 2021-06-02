T = int(input())
node = []
h_1 = []
h_2 = []
for i in range(T):
	node.append(input())

for i in range(len(node)):
    node[i]=node[i].split(' ~ ')
    for j in range(len(node[i])):
        node[i][j]=list(map(int,node[i][j].split(':')))

for i in range(len(node)):
    h_1.append(node[i][0])
    h_2.append(node[i][1])


if max(h_1) < min(h_2):
    if max(h_1)[1] == 0:
        max(h_1)[1] = "00"
    if min(h_2)[1] == 0:
        min(h_2)[1] = "00"
    print(str(f"{max(h_1)[0]}:{max(h_1)[1]} ~ {min(h_2)[0]}:{min(h_2)[1]}"))
else:
    print(-1)

            