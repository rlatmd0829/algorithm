# n = int(input())

# def hanoi(n, start, mid, end): 
#     if n == 1:
#         print(start,end)
#     else:
#         hanoi(n-1, start, end, mid) # 원판 1에서 3거쳐서 2로 옮김
#         print(start,end) # 원판 1에서 원판 3으로 옮김
#         hanoi(n-1, mid, start, end) # 원판 2에서 1거쳐서 3으로 옮김
        

# sum =1
# for i in range(n-1):
#     sum = sum*2 +1
# print(sum)
# hanoi(n,1,2,3)


########

def hanoi_tower(n, start, end):
    if n==1:
        print(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계

n = int(input())
print(2**n-1)
hanoi_tower(n,1,3)