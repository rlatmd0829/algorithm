from collections import Counter

def solution(n, results):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # 알수 없을경우 0
    for x,y in results: # 이겼을경우 1, 졌을경우 -1
        graph[x][y] = 1
        graph[y][x] = -1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                    elif graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1

    ans = 0
    print(graph)
    for i in range(1,n+1):
        print(Counter(graph[i])) # graph[i] 원소에 대한 숫자를 세어준다.
        print(Counter(graph[i])[0]) # graph[i]에 0에 갯수를 세어준다.
        if Counter(graph[i])[0] == 2: # 인덱스 n+1로 만들어서 인덱스0이랑, 자기자신을 포함해 0이 2개만 있으면 i는 순위를 알 수 있다.
            ans += 1
    return ans