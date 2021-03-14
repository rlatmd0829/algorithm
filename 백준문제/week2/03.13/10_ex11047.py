N, K = map(int, input().split())

d = [int(input()) for _ in range(N)]

d.sort(reverse=True)

result = 0
for i in range(N):
    if d[i] > K:
        continue
    else:
        result += K // d[i]
        K = K % d[i]
print(result)

# 그리디 알고리즘 문제
# 눈앞에 최적의 해를 선택하기 위해 가장 큰 수부터 진행해보기 위해 리스트를 거꾸로 정렬해준다.
# K의 값보다 나눠야 하는 값이 크다면 넘어간다.
# K와 같거나 작은 수중에 가장 큰수로 나눠준다.