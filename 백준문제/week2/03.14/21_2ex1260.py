# dfs bfs  인접행렬로 풀어보기

n, m, v = map(int, input().split())
node = [[0] * (n+1) for _ in range(n+1)]


for i in range(m):
    line = list(map(int, input().split()))
    
    node[line[0]][line[1]] = 1
    node[line[1]][line[0]] = 1

print(node)


def dfs (node, start, visited):
    visited.append(start)
    for i in range(1, n+1): # 정점이 0이 없고 1~n까지 밖에 없어서 1이 있을곳은 1~n까지 이기때문에 범위를 이렇게 잡는다.
        if node[start][i] and i not in visited: # node[start][i] 가 1이어야한다.
            visited = dfs(node, i, visited)
    return visited

def bfs(node, start):
    q = [start]
    visited = [start]
    while q:
        current_node = q.pop(0)
        for i in range(1, n+1):
            if node[current_node][i] and i not in visited:
                q.append(i)
                visited.append(i)
    return visited


print(' '.join(map(str, dfs(node, v, []))))
print(' '.join(map(str, bfs(node, v))))

