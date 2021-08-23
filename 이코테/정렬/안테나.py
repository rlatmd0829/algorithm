n = int(input())

value = list(map(int,input().split()))

value.sort()

print(value[(n-1)//2])