# 투포인터 문제
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
tmp_sum = 0
min_length = sys.maxsize

# start = 0, end = 1일때 tmp_sum에는 arr[0] 값만 들어가있다. end값 전까지에 합이 들어간다 생각하자.
while True:
    if tmp_sum >= S: # 원하는 값보다 크거나 같다면 start를 움직인다.
        min_length = min(min_length, end - start)
        tmp_sum -= arr[start]
        start += 1

    elif end == N:
        break

    else: # 원하는 값보다 작다면 end를 움직인다.
        tmp_sum += arr[end]
        end += 1
    
if min_length == sys.maxsize:
   print(0)
else:
   print(min_length)