import sys
sys.setrecursionlimit(10**6)
n, s = map(int, input().split())

value = list(map(int, input().split()))

count = 0

def recursive(index,sum):
    global count
    if index == n:
        if sum == s:
            count += 1
        return
    
    recursive(index+1, sum + value[index])
    recursive(index+1, sum)
    
recursive(0,0)
if s == 0:
    count -= 1
print(count)
