# 백트래킹은 dfs의 방식을 기반으로, 불필요한 경우를 배제하며 원하는 해답에 도달할 때 까지 탐색하는 전략
# N,M (1) 

# N,M = map(int, input().split())
# visited = [0 for _ in range(N)]
# arr = []

# def dfs(cnt):
#     print(*arr)
#     return

#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             arr.append(i+1)

#             dfs(cnt+1) 

#             visited[i] = 0
#             arr.pop()

# dfs(0)

########################

# 순열 라이브러리 사용
# from itertools import permutations

# N, M  = map(int, input().split())

# p = permutations(range(1, N+1),M)
# for i in p:
#     print(*i)



#########################

# N,M (2) 

N, M = map(int, input().split())
visited = [0 for _ in range(N)]
arr = []
print(visited)

def dfs(cnt):
    print(arr)
    if cnt == M:
        print(*arr)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1 # 중복제거
            arr.append(i+1)

            dfs(cnt+1) # 다음 깊이 탐색
            
            arr.pop()

            #순열 부분과의 차이점, i보다 큰값만 출력하기 위해 0으로만들어줌
            for j in range(i+1, N):
                visited[j] = 0
    

dfs(0)

###############################

# 조합 라이브러리 사용

# from itertools import combinations

# N,M = map(int, input().split())

# p = combinations(range(1, N+1),M)
# for i in p:
#     print(*i)