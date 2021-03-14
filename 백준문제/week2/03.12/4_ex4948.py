# import math

# result=[]

# def c(a,b):
#     cnt=0
#     for i in range(a+1,b+1): 
#         for j in range(2,int(math.sqrt(i)+1)):
#             if i % j == 0:
#                 break
#         else:
#             cnt+=1
#     return cnt

# while True:
#     a=int(input())
#     if a==0:
#         break
#     result.append(c(a,2*a))


# for i in result:
#     print(i)



######################################

import math
import sys

result=[]

def c(a,b):
    cnt=0
    check = [True] * (b+1) 
    
    for i in range(2,int(math.sqrt(b)+1)):
        if check[i] == True:
            for j in range(i*2, b+1, i):
                check[j] = False
    
    for i in range(a+1,b+1): # a보다 크고 b보다 작은 수를 구하기 때문에 3<x<7 x=4,5,6 3개
        if check[i] == True:
            cnt += 1
    return cnt

while True:
    a=int(sys.stdin.readline().strip())
    if a==0:
        break
    result.append(c(a,2*a))
    


for i in result:
    print(i)

#############################################
#입력이 들어올때마다 에라토스테네스의 체를 돌리는것은 비효율적이다.
#문제에 범위내에 모든 수에 대해서 소수를 구하고 확인하는 것이 훨씬 빠르다
#밑에 코드가 훨씬 빠름

# import sys
# import math

# # 1 <= n <= 123456
# # 모든 수가 소수인것으로 초기화, 1은 소수가 아님
# array = [True] * 246913

# #에라토스테네스의 체
# # 2부터 n의 제곱근 까지의 모든 수를 확인
# for i in range(2, int(math.sqrt(246912))+1):
#     if array[i] == True:
#         for j in range(i*i, 246913, i):
#             array[j] = 0

# while True:
#     n = int(sys.stdin.readline().strip())
#     if n == 0:
#         break
#     print(sum(array[n+1:2*n+1]))
