# import math
# a,b = map(int,input().split())

# for i in range(a,b+1):
#     if(i==1):
#         continue
#     n=int(math.sqrt(i))
#     for j in range(2,n+1):
#         if i%j == 0:
#             break
#     else:
#         print(i)

# m, n = map(int, input().split())

# def isprime(m,n):
#     n += 1
#     prime = [True] * n
#     for i in range(2, int(n**0.5)+1):
#         if prime[i]:
#             for j in range(2*i, n, i):
#                 prime[j] = False
    
#     for i in range(m,n):
#         if i > 1 and prime[i] == True:
#             print(i)


# isprime(m,n)



n,m = map(int, input().split())

def isprime(n,m):
    check = [True] * (m+1) 
    for i in range(2, int(m**0.5)+1): # 2 3 제곱근 4
        if check[i] == True:
            for j in range(i*2, m+1, i): # 4 6 8 10 12 ..
                check[j] = False         # 6 9 12 15 18 ...
            
    for i in range(n,m+1):
        if i > 1 and check[i] == True:
            print(i)

isprime(n,m)
