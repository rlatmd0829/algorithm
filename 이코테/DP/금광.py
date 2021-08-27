t = int(input())


for k in range(t):
    n, m = map(int, input().split())
    
    result = 0
    value = list(map(int, input().split()))
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(value)):
        graph[i//m][i%m] = value[i]
    print(graph)

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                graph[j][i] += max(graph[j][i-1], graph[j+1][i-1])
            elif j == n-1:
                graph[j][i] += max(graph[j][i-1], graph[j-1][i-1])
            else:
                graph[j][i] += max(graph[j][i-1], graph[j-1][i-1], graph[j+1][i-1])
    
    for i in graph:
        result = max((result,max(i)))

    print(result)