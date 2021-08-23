# 투포인터로 풀어보기

n, m = map(int, input().split())

value = list(map(int, input().split()))

l, r = 0, 1
total = value[0]
answer = 0
while True:

    if m == total:
        answer += 1
    
    if r == n and total < m:
        break

    if m > total:
        total += value[r]
        r += 1
    else:
        total -= value[l]
        l += 1

    
    
print(answer)