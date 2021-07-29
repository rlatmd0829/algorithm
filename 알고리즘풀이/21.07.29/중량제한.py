import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y,w = map(int, input().split())
    graph[x].append((y,w))
    graph[y].append((x,w))

start, end = map(int, input().split())

def bfs(c):
    visited = [False for _ in range(n+1)]
    queue = collections.deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for next, w in graph[cur]:
            if visited[next] == False:
                if w >= c:
                    visited[next] = True
                    queue.append(next)
    return True if visited[end] == True else False

l = 1
r = 1000000000
check = 0
while l <= r:
    mid = (l+r) // 2
    if bfs(mid):
        check = mid
        l = mid + 1
    else:
        r = mid - 1
print(check)

