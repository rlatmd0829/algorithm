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

# N, M = map(int, input().split())
# visited = [0 for _ in range(N)]
# arr = []
# print(visited)

# def dfs(cnt):
#     print(arr)
#     if cnt == M:
#         print(*arr)
#         return
    
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1 # 중복제거
#             arr.append(i+1)

#             dfs(cnt+1) # 다음 깊이 탐색
            
#             arr.pop()

#             #순열 부분과의 차이점, i보다 큰값만 출력하기 위해 0으로만들어줌
#             for j in range(i+1, N):
#                 visited[j] = 0
    

# dfs(0)

###############################

# 조합 라이브러리 사용

# from itertools import combinations

# N,M = map(int, input().split())

# p = combinations(range(1, N+1),M)
# for i in p:
#     print(*i)

#############################

def makeS(L):
    # 주어진 M만큼 수열을 만들게 되었을 때 출력
    if L == M:
        for i in range(L):
            print(S[i], end=" ")
        print()
    else:
        # 1부터 N까지의 수열 만들기
        for j in range(1, N+1):
            #해당 숫자를 사용하지 않은 경우
            if check[j] == 0:
                #해당 수 이하를 체크하기
                for k in range(j + 1):
                    check[k] = 1
                # 수열에 숫자 넣기
                S[L] = j
                # 숫자 하나 고르기
                makeS(L + 1)
                # 돌아온 시점에서 다시 전부 초기화
                for k in range(j + 1):
                    check[k] = 0

# 자연수 N, M
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순
N, M = map(int, input().split())

# 만들 수열을 담을 리스트
S = [0] * N

#인덱스가 수열의 숫자를 표시하는 체크리스트
check = [0] * (N+1)

makeS(0)