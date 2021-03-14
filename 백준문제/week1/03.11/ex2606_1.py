computer = int(input())
network = int(input())
virus_map = [[0 for _ in range(computer + 1)] for _ in range(computer + 1)]
print(virus_map)
#2차원 배열 안에 넣어주기
for _ in range(network):
    x, y = map(int, input().split()) #번호가 0부터 시작안하고 1부터 7까지 이기 때문에 virus_map[0] 은 의미없는 배열이다.
    virus_map[x][y] = 1              
    virus_map[y][x] = 1

print(virus_map)

def bfs(virus_map, start):
    queue = [start]
    visited = []

    while queue:
        temp = queue.pop(0)
        visited.append(temp)

        for i in range(len(virus_map)):
            # 인접행렬은 0인경우도 다 넣어줬기 때문에 1인경우 만 실행할 수 있도록 해줘야 하고 인접리스트 같은 경우는 1인경우만 들어있기 때문에 따로 처리 해줄 필요없다.
            # virus_map[temp][i] 가 true인 경우에만 즉, 1인경우에 실행한다.
            if virus_map[temp][i] and i not in visited and i not in queue: # i not in queue 를 추가해서 중복을 제거해준다.
                queue.append(i)
                

    return len(visited)-1 # 1을 제외한 감염된 노드 수 출력

print(bfs(virus_map, 1))