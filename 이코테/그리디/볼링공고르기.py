n, m = map(int, input().split())

bow = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if bow[i] != bow[j]:
            count += 1
print(count)

#########################

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 자기 자신 무게 제외
    result += array[i] * n 
print(result)