from collections import deque
N = int(input()) # 1,2,3,4,5,6

q = deque(i for i in range(1,N+1)) # q([1,2,3,4,5,6])
print(q)
while q:
    a=q.popleft()
    q.rotate(-1)

print(a)
