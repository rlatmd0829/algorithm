import sys
from collections import deque
N = int(input())

queue = deque()

def push(X):
    queue.append(X)

def pop():
    if not queue:
        return -1
    return queue.popleft()

def size():
    return len(queue)

def empty():
    if queue:
        return 0
    else:
        return 1

def front():
    if not queue:
        return -1
    return queue[0]

def back():
    if not queue:
        return -1
    return queue[-1]

for i in range(N):
    a=sys.stdin.readline().split()
    if a[0] == 'push':
        push(int(a[1]))
    elif a[0] == 'pop':
        print(pop())
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'empty':
        print(empty())
    elif a[0] == 'front':
        print(front())
    elif a[0] == 'back':
        print(back())
    