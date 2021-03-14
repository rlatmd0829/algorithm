# 출력 : 토마토가 모두 익을 때까지의 최소날짜 출력
#        만약, 저장될 때 부터 모든 토마토가 익어있는 상태라면 0출력
#        토마토가 모두 익지는 못하는 상황이면 -1출력

from collections import deque
checker = True 
M, N   = list(map(int, input().split())) # M : 넓이 , N : 높이
tomato = [] 
for _ in range(N):
    tomato.append(list(map(int, input().split()))) # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]


q = deque() # 익은 토마토를 담을 큐 생성

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1: # 익은 토마토 큐에 추가
            q.append([i,j]) # deque([[3,5]])


dx = [0,0,1,-1] 
dy = [1,-1,0,0]
# dx[0],dy[0] = (0,1) 오른쪽
# dx[1],dy[1] = (0,-1) 왼쪽
# dx[2],dy[2] = (1,0) 아래쪽
# dx[3],dy[3] = (-1,0) 위쪽

time = -1   # 출력값 : 걸린 날짜
            # -1로 시작하는 이유는 bfs로 검사 했을경우 이미 다 익은 토마토인 경우에는 걸린날짜 0을 리턴해주기 위함

# bfs   
def bfs(q, time):    
    while q: # 큐가 빌때 까지 계속 돌음
        time += 1 
        for _ in range(len(q)): # 큐에 길이만큼 반복 왜냐하면 익은 토마토가 여러개 있을 수 있기 때문에
            a, b = q.popleft()
            
            for i in range(4):  # 상하좌우 확인
                nx = a + dx[i]
                ny = b + dy[i]
                
                if (0 <= nx < N) and (0 <= ny < M) and tomato[nx][ny] == 0: # 범위가 안넘어가면서 안익은 토마토일 경우 큐에 추가하고 익혀줌
                    q.append([nx, ny])
                    tomato[nx][ny] = 1
    return time

time = bfs(q, time)
               

for i in tomato: # tomato = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
    if 0 in i: # i안에 0이 있을경우는 토마토가 모두 익지 못한경우이다.
        checker = False
        print(-1) # -1 출력
        break

if checker:
    print(time)