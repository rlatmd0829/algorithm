# 위상정렬 순으로만 출력하면 되고 같은순서에 대해선 따로 언급이 없으므로 따로 우선순위큐는 사용하지 않아도 된다.
import collections
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

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
    print(cur, end = ' ')
    for next in graph[cur]:
        distance[next] -= 1
        if distance[next] == 0:
            queue.append(next)        
