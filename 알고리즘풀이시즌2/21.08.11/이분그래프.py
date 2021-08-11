import collections
t = int(input())


for i in range(t):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for j in range(E):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    queue = collections.deque()
    def bfs(start):
        queue.append(start)
        visited[start] = 1
        while queue:
            cur = queue.popleft()
            for next in graph[cur]:
                if visited[next] == 0:
                    visited[next] = visited[cur] * -1
                    queue.append(next)
                elif visited[next] == visited[cur]:
                    return False
        return True

        
    for j in range(1, V+1):
        if visited[j] == 0:
            check = bfs(j)
            if check == False:
                break
    if check:
        print("YES")
    else:
        print("NO")

    