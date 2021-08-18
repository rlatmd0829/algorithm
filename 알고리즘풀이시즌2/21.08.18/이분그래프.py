import collections
t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    for j in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    queue = collections.deque()
    result = []
    
    def bfs(start):
        queue.append(start)
        check[start] = 1
        while queue:
            cur = queue.popleft()
            for next in graph[cur]:
                if check[next] == 0:
                    check[next] = check[cur] * -1
                elif check[next] == check[cur]:
                    return False
        return True

    for j in range(1, n+1):
        if check[j] == 0:
            chk = bfs(j)
            if chk == False:
                break
    if check:
        print("YES")
    else:
        print("NO")