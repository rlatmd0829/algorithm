# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28
# 0  1  2  3  4  5  6  7  8  9  10  11  12  13

# 3 = 1(0) + 2(4)
# 4 = 1(1) + 3(5)
# 5 = 1(2) + 4(6)
# 7 = 2(3) + 5(7)
# 9 = 2(4) + 7(8)
# 12 = 3(5) + 9(9)
# 16 = 4(6) + 12(10)

T = int(input())


for i in range(T):
    
    a=int(input())
    result = [0] * (a)
    
    for j in range(a):
        if j <= 2:
            result[j] = 1
        elif j <= 4:
            result[j] = 2
        else:
            result[j] = result[j-5] + result[j-1]
            
    print(result[a-1])
