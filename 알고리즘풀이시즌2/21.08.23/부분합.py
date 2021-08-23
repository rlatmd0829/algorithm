import sys
n, m = map(int, input().split())

value = list(map(int, input().split()))
minn = sys.maxsize
l, r = 0,1
total = value[0]

while True:

    if r == n and m >= total:
        break

    if m > total:
        total += value[r]
        r += 1
    else:
        minn = min(minn, r - l)
        total -= value[l]
        l += 1

if minn == sys.maxsize:
    print(0)
else:    
    print(minn)