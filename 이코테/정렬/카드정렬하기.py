import sys
import heapq

n = int(input())
answer = 0
value = [int(input()) for _ in range(n)]


if n == 1:
    print(0)
else:
    while len(value) != 1: # len(value) 가 1이라는 소리는 모든 값을 다 빼서 더해본 상태라는 의미이다.
        min1 = heapq.heappop(value)
        min2 = heapq.heappop(value)
        answer += min1 + min2
        heapq.heappush(value, min1 + min2)
    print(answer)