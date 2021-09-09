def solution(N, relation, dirname):
    answer = ['root']
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    result = []
    for a,b in relation:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(index):
        visited[index] = True
        
        for next in graph[index]:
            if visited[next] == False:
                answer.append(dirname[next-1])
                print(answer)
                result.append(answer)
                
                dfs(next)
                answer.pop()
        return result
            
        
        
    result = dfs(1)
    print(result)
    return answer