import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
result = [1 for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    distance[y] += 1

queue = collections.deque()

for i in range(1,n+1):
    if distance[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    for next in graph[cur]:
        distance[next] -= 1
        if distance[next] == 0:
            queue.append(next)
            result[next-1] = result[cur-1] + 1
            
print(*result)
