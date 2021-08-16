n = int(input())

gauss = [i*(i+1)//2 for i in range(1,46)]
check = [0] * 1001

for i in gauss:
    for j in gauss:
        for k in gauss:
            if i+j+k <= 1000:
                check[i+j+k] = 1
for i in range(n):
    print(check[int(input())])

# 재귀풀이 시간초과

#  n = int(input())

# value = [int(input()) for _ in range(n)]
# check = [0] * 1001
    
# gauss = [i*(i+1)//2 for i in range(1,46)]

# def recursive(index,sum,count):
#     if count == n:
#         if sum <= 1000:
#             check[sum] = 1
#         return
#     if index == len(gauss):
#         return

#     recursive(index+1, sum + gauss[index], count+1)
#     recursive(index+1, sum, count)

# recursive(0,0,0)

# for i in value:
#     print(check[i])
