# N, M = map(int,input().split())
# a = list(map(int,input().split()))

# start, end = 1, max(a) # 이분탐색 검색범위 설정

# while start <= end:
#     mid = (start+end) // 2

#     log = 0 # 벌목된 나무 총합
#     for i in a:
#         if i >= mid:
#             log += i - mid

#     #벌목 높이를 이분탐색
#     if log >= M:
#         start = mid + 1 # 벌목 나무가 과하다면 절단기 높이를 높여서 조금만 가져가게함
#     else:
#         end = mid - 1 # 벌목 나무가 부족하다면 절단기 높이를 낮춰서 더 많이 가져 갈수 있게함
# print(end) # 왜 end 출력하는지 이해안감


#########################

# 자르는 높이를 이진 탐색하기
# n: 나무의 수, m: 가지고 갈 나무의 길이
n, m = map(int, input().split())
# 나무의 높이
trees = list(map(int, input().split()))
# 자르는 높이의 시작점
start = 1
# 결과값
res = 0
# 자르는 높이의 끝점
end = max(trees)

while start <= end:

    # 자르는 높이의 중간점(절단기의 현재 높이)
    mid = (start + end) // 2
    cut = 0
    for tree in trees:
        if tree > mid:
            cut += tree - mid
    # 더 잘렸거나 맞게 잘랐을 때
    if cut >= m:
        start = mid + 1
        # 최댓값 구하기
        if res < mid:
            res = mid
    # 덜 잘렸을 때
    elif cut < m:
        end = mid - 1
print(res)