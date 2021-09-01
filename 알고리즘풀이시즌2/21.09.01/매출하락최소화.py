import collections
def solution(sales, links):
    answer = 0
    leng = len(sales)
    graph = [[] for _ in range(leng+1)]
    visited = [False for _ in range(leng+1)]
    distance = [0 for _ in range(leng+1)]
    # for i in range(leng):
    #     graph[i+1].append(sales[i])
    for a,b in links:
        graph[a].append(b)
    
    queue = collections.deque()
    queue.append(1)
    def bfs():
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for next in graph[cur]:
                if visited[next] == False:
                    distance[next] = distance[cur] + 1
                    visited[next] = True
                    queue.append(next)
    bfs()
    for i in range(1,leng+1):
        distance[i]
        
    print(distance)
                    
        
        
    
        
    return answer