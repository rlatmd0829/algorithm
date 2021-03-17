# def quad_tree(x, y, n):
#     global blue, white
#     color = matrix[y][x] # 리스트에서 [][] 앞에 값이 이중리스트 안에 어떤 리스트인지를 결정하기때문에 좌표개념에 y랑 같은뜻이다.
#     double_break = False
    
#     for i in range(x, x+n):
#         if double_break:
#             break
#                 # [ [],[],[] ] list[0][1]
#         for j in range(y, y+n):
#             if matrix[j][i] != color: # 하나라도 틀릴시에 재귀문 생성
#                 quad_tree(x, y, n//2) # 2사분면
#                 quad_tree(x + n//2, y, n//2) # 1사분면
#                 quad_tree(x, y + n//2, n//2) # 3사분면
#                 quad_tree(x + n//2, y + n//2, n//2) # 4사분면
#                 double_break = True # 탈출
#                 break
        
#     if not double_break: # double_break가 false일 경우
#         if matrix[y][x] == 1: # 맨위 for문이 끝났고 여기 왔다는 소리는 matrix[y][x]랑 범위안에 있는 것들이 전부 같다는 뜻이므로 한개만 확인하면 된다.
#             blue += 1
#         else:
#             white += 1 # 흰색이라면

# N = int(input())

# matrix = [list(map(int,input().split())) for _ in range(N)]


# blue = 0
# white = 0

# quad_tree(0,0,N)
# print(white)
# print(blue)

# 분할정복과 동적계획법은 비슷하지만 다른 개념이다.
# 일단 둘 다 반복과 재귀를 이용하며 Top-down 이나 Bottom-up방식을 통해서 문제를 해결한다.
# 동적 계획법은 작게 나눈 부분들을 해결해가면서 결과를 더 큰 부분을 푸는데 이용한다.
# 이때 분할되는 과정에서 작은 부분들이 중복되어서 여러 번 반복되어 나올 수 있기 때문에 memoization도 같이 사용한다.
# 분할 정복도 문제를 풀 수 있는 가장 작은 단위의 문제로 만든 다음에 해결하고 병합하는 과정들을 한다.
# 차이점은 동적 계획법과 달리 sub problems의 중복이 없다.

# import sys

# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# result = []

# def solution(x,y,N):
#     color = paper[x][y]
#     for i in range(x, x+N):
#         for j in range(y, y+N):
#             if color != paper[i][j]:
#                 solution(x, y, N//2)
#                 solution(x, y+N//2, N//2)
#                 solution(x+N//2, y, N//2)
#                 solution(x+N//2, y+N//2, N//2)
#                 return
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)

# solution(0,0,N)
# print(result.count(0))
# print(result.count(1))


#########################################

import sys

n = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

w_cnt = 0
b_cnt = 0

def func(x,y,k):
    global w_cnt, b_cnt
    temp_cnt = 0

    for i in range(x, x+k):
        for j in range(y, y+k):
            if graph[i][j]: # graph[i][j] == 1 과 동일
                temp_cnt += 1

    if not temp_cnt: # temp_cnt == 0과 동일
        w_cnt += 1
    elif temp_cnt == k ** 2:
        b_cnt += 1
    else:
        func(x,y,k//2)
        func(x+k//2, y, k//2)
        func(x, y+k//2, k//2)
        func(x+k//2, y+k//2, k//2)
    return

func(0,0,n)
print(w_cnt)
print(b_cnt)