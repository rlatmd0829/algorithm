# 정답 풀이가 아님 플로이드 워샬로 풀어보기
import collections
def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    result = [0 for _ in range(n+1)]
    for x,y in results:
        graph[x].append(y)
    print(graph)
    queue = collections.deque()
    
    def bfs(index):
        queue.append(index)
        while queue:
            cur = queue.popleft()
            for next in graph[cur]:
                distance[next] = distance[cur] + 1
                queue.append(next)
                
    for i in range(1, n+1):
        distance = [0 for _ in range(n+1)]
        bfs(i)
        for idx,i in enumerate(distance):
            if i > 0:
                result[idx] += 1
    
    result.pop(0)
    print(result)
    for i in result:
        print(result.count(i))
        
    
        
    return answer