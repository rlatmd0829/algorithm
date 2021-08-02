# 잘모르겠다.
import collections
t = int(input())

for i in range(t):
    k,m,p = map(int, input().split())
    graph = [[] for _ in range(m+1)]
    distance = [[0,0,0] for _ in range(m+1)] # [[진입차수, 최대레벨, 최대레벨 갯수],[]]
    check = [1 for _ in range(m+1)]
    for j in range(p):
        x,y = map(int, input().split())
        graph[x].append(y)
        distance[y][0] += 1
    
    queue = collections.deque()

    for j in range(1, m+1):
        if distance[j][0] == 0:
            queue.append(j)
            distance[j][1] = 1

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            distance[next][0] -= 1
            if distance[next][1] < distance[cur][1]:
                distance[next][1] = distance[cur][1]
                distance[next][2] = 1
            elif distance[next][1] == distance[cur][1]:
                distance[next][2] += 1
            if distance[next][0] == 0:
                if distance[next][2] > 1:
                    distance[next][1] += 1
                queue.append(next)
    print(k, distance[m][1])