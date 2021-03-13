N = int(input())

time = list(map(int, input().split()))
time.sort()
sum=0
for i in range(N):
    for j in range(i+1): # i가 0~4까지들어오기 때문에 +1을 해줘서 i가 0일떄도 for문이 돌아 가게 하고 j도 4까지 하기 위해 1을 더한 것이다
        sum += time[j]
print(sum)

# 12334
# 1+3+6+9+13

# 그리디 알고리즘 문제
# 매 순간마다 최적의 해를 선택한다. 그러면 결과가 최적의 결과가 아닐 수 있지만
# 정렬된 경우 같은 특정한 순간에는 눈앞에 최적의 해를 구하는것이 결과가 최적의 해 일 수 있다.
