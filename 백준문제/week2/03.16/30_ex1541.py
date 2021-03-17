
N = input().split('-')  # 입력값을 '-'를 기준으로 입력받는다. ex) ['55', '50+40'] 
                        # 최솟값을 찾기 위해서는 '-' 이전 이후로 나눠서 연산을 해준뒤에 계산하면 최솟값이 나온다.
result = []             
for i in N:
    result.append(list(map(int,i.split('+'))))
                        # '+'연산자로 묶인 것들은 더해 주기 위해서 리스트에 넣어준다. ex) [[55], [50,40]]

Sum = []
for i in result:
    cnt = 0
    for j in i:
        cnt += int(j)
    Sum.append(cnt)     # Sum에 계산한 값들을 넣어준다. [55, 90]
                        # Sum에 있는 수들은 모두 '-'를 기준으로 나눠져 있는 수들이다

total = Sum[0]          # '-' 이전값에서 이후값을 빼주기 위해서 total에 먼저 이전값을 넣어준다.
for i in range(1,len(Sum)):
    total -= Sum[i]

print(result)
