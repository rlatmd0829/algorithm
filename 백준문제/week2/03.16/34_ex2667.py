import sys

input = sys.stdin.readline

def dfs(x, y):
    global count
    if x <= -1 or x >= N or y <= -1 or y >= N: # 범위값에 안맞으면 바로 false
        return False
    if graph[x][y] == 1:
        count += 1 # 단지안에 아파트 수를 세줌
        graph[x][y] = 0 # 1인 것을 검사 두번하지 않기 위해서 0으로 만들어줌
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().strip())))

result = 0
danji = []
count = 0

for i in range(N): # 모든 행 검사
    for j in range(N): # 모든 열 검사
        if dfs(i,j) == True:
            result += 1
            danji.append(count) # 재귀를 다돌고 나온 count수를 danji에 저장해줌
            count = 0 # 카운트수 초기화
print(result) # 총 단지수 출력
danji.sort() # 오름차순으로 정렬
for d in danji:
    print(d)