import math
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# sum=0
# cnt=0
# while True:
#     cnt += 1
#     sum += 2
#     if sum == c:
#         break
#     else:
#         sum -= 1
    
# print(cnt)


###################

A,B,V = map(int,input().split())
x = math.ceil((V-B)/(A-B))
print(x)

# V <= A*x - B*x + B
# V/x - B/x <= A - B
# (V-B)x <= A-B
# V-B <= (A-B)x
# x >= V-B/(A-B)
# x = math.ceil((V-B)/(A-B))
        


