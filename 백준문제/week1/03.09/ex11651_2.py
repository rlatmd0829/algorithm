# T = int(input())

# a =[]
# for i in range(T):
#     [x, y] = map(int, input().split())
#     re = [y, x]
#     a.append(re) # [[y,x], [y,x]]

# a.sort()
# for i in range(T):
#     print(a[i][1], a[i][0])

###################################################


# def abc(x):
#     return (x[1], x[0])

T = int(input())
a = []

for i in range(T):
    a.append(list(map(int, input().split()))) # [[x,y], [x,y], [x,y]]
a.sort(key=abc) # a 인자값을 abc로 보내서 리턴값으로 비교후 정렬
for i in a:
    print(i[0], i[1])

# lambda x : (x[1], x[0]) == def abc(x):
#                               return (x[1], x[0]) 


