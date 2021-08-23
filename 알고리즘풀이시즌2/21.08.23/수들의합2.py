# 투포인터로 풀어보기

n, m = map(int, input().split())

value = list(map(int, input().split()))

l, r = 0, 1
total = value[0]
answer = 0
while True:

    if m == total: # 위에 써줘야 하는 이유는 total에 value[0]을 넣고 시작하기 떄문에 먼저 확인해줘야 한다.
        answer += 1
    
    if r == n and total <= m: # r == n 이더라도 total이 m보다 크거나 같다면 l을 줄이면서 또 확인이 가능하기 때문에
                            # r==n 이고 total이 m보다 작은 경우만 종료한다.
                            # value 안에 값이 1보다 큰 수 이므로 total == m이랑 같아도 끝낸다.
        break

    if m > total:
        total += value[r]
        r += 1
    else:
        total -= value[l]
        l += 1

    
    
print(answer)