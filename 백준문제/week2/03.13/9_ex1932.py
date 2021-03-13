T = int(input())
q = []

for i in range(T):
    q.append(list(map(int,(input().split()))))

for i in range(1,T):
    for j in range(len(q[i])):
        if j==0: # 맨왼쪽
            q[i][j] += q[i-1][j]
        elif j==i: # 맨오른쪽
            q[i][j] += q[i-1][j-1]
        else: # 가운데
            q[i][j] += max(q[i-1][j], q[i-1][j-1])

print(max(q[T-1]))

# 최적의 해를 찾기 위해서 위에서부터 더하면서 내려온다
# 맨왼쪽과 맨 오른쪽은 더할수 있는 값이 한개이기 때문에 더해주고
# 가운데 값들은 두개중 큰값을 더해 나간다.

#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5 

#      7
#    10 15
#   18 16 15
#  20 25 20 19
# 24 30 27 26 24