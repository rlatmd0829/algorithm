import sys, collections

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[]for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

check = False
q = collections.deque([])
q.append(start)
distance[start] = 0
while q:
    cur = q.popleft()
    if cur == end:
        check = True
        break
    for next in graph[cur]:
        if distance[next] == -1:
            distance[next] = distance[cur] + 1
            q.append(next)
if check:
    print(distance[cur])
else:
    print(-1)

