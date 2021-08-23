import sys
n, m = map(int, input().split())

value = list(map(int, input().split()))
minn = sys.maxsize
l, r = 0,1
total = value[0]

while True:

    if r == n and m > total: # m >= total로 하면 안되는 이유는 value 안에 값에 0이 있을 수 있기 떄문인것 같다.
        break

    if m > total:
        total += value[r]
        r += 1
    else: # total이 m 이상이 되는 값중 최솟값에 길이를 구하기 때문에 total == m 일때만 minn을 구하면 안된다.
        minn = min(minn, r - l) 
        total -= value[l]
        l += 1

if minn == sys.maxsize:
    print(0)
else:    
    print(minn)