import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
queue = deque(range(1, n+1))

total = 0

for idx in range(m):
    if numbers[idx] == deque[0]:
        queue.popleft()
        continue
    queue_idx = queue.index(numbers[idx])

    # 뒤 -> 앞으로 옮기는게 이득인 경우
    if queue_idx > len(queue) // 2:
        queue.rotate(len(queue) - queue_idx)
        total += (len(queue) - queue_idx)

    # 앞 -> 뒤로 옮기는게 이득인 경우
    elif queue_idx <= len(queue) //2:
        queue.rotate(-queue_idx)
        total += queue_idx
    queue.popleft()

print(total)