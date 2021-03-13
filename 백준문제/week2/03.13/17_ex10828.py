import sys
N = int(input())
stack = []
a = []

def push(X):
    stack.append(X)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

# false = 0, true =1

def empty():
    if stack: 
        return 0
    else: 
        return 1

def top():
    if not stack:
        return -1
    else:
        return stack[-1]

for i in range(N):
    a=sys.stdin.readline().split()
    if a[0] == 'push':
        push(int(a[1]))
    elif a[0] == 'top':
        print(top())
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'empty':
        print(empty())
    elif a[0] == 'pop':
        print(pop())