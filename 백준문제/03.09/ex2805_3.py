N, M = map(int,input().split())
a = list(map(int,input().split()))

start, end = 1, max(a) # 이분탐색 검색범위 설정

while start <= end:
    mid = (start+end) // 2

    log = 0 # 벌목된 나무 총합
    for i in a:
        if i >= mid:
            log += i - mid

    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1 # 벌목 나무가 과하다면 절단기 높이를 높여서 조금만 가져가게함
    else:
        end = mid - 1 # 벌목 나무가 부족하다면 절단기 높이를 낮춰서 더 많이 가져 갈수 있게함
print(end)