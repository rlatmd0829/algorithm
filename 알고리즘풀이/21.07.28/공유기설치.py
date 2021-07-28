n, c = map(int, input().split())
share = [int(input()) for _ in range(n)]

share.sort()

l = 0
r = share[-1] - share[0]
check = 0

while l <= r:
    mid = (l + r)//2  # 공유기 설치 거리
    current = share[0]
    count = 1
    for i in range(1, n):
        if share[i] >= current + mid:
            count += 1
            current = share[i]

    if count >= c: # 이미 충족이 됬다면 공유기 설치 거리를 늘려서 최대값을 찾는다.
        check = mid
        l = mid + 1
    else:
        r = mid - 1
print(check)