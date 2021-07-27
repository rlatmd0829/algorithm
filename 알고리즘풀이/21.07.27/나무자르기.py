n, m = map(int, input().split())
h = list(map(int, input().split()))
l = 1
r = max(h)
check = 0
while l <= r:
    ans = 0
    mid = (l + r) // 2
    for i in h:
        if i > mid:
            ans += i - mid
    if ans >= m:
        l = mid + 1
        check = mid
    else:
        r = mid - 1
print(check)
