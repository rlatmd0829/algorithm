def solution(info, edges):
    answer = 0
    maxx = 0
    graph = [[] for _ in range(len(info))]
    visited = [False for _ in range(len(info))]
    distance = [0,0]
    print(distance)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(index):
        nonlocal answer
        answer = max(answer, distance[0])
        visited[index] = True
        if info[index] == 0:
            #print(distance[0])
            distance[0] += 1
        else:
            #print(distance[1])
            distance[1] += 1
        for next in graph[index]:
            #print(next)
            if visited[next] == False:
                if distance[0] <= distance[1]:
                    return
                else:
                    dfs(next)
                    # visited[next] = False
                    # if info[next] == 0:
                    #     distance[0] -= 1
                    # else:
                    #     distance[1] -= 1
                
    dfs(0)
    return answer