# 시간초과 pypy로 제출

n, m = map(int, input().split())

value = list(map(int,input().split()))

l = 1
r = max(value)
check = 0
while l <= r:
    answer = 0
    mid = (l+r) // 2

    for i in value:
        if i > mid:
            answer += i - mid
    
    if answer >= m:  # 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다.
                     # answer == m 일때가 가장 높이가 큰경우 아닌가..?
        l = mid + 1
        check = mid
    else:
        r = mid - 1
print(check)


### 자르는 부분 함수로 뺴면 시간초과 안난다.. 신기

# n, m = map(int, input().split())
# value = list(map(int, input().split()))
# l = 1
# r = max(value)
# check = 0

# def sumCut(mid):
#     answer = 0
#     for i in value:
#         if i > mid:
#             answer += i - mid
#     return answer

# while l <= r:
#     mid = (l + r) // 2
#     answer = sumCut(mid)
#     if answer >= m:
#         l = mid + 1
#         check = mid
#     else:
#         r = mid - 1
# print(check)
