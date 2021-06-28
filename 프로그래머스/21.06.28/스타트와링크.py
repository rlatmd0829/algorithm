from itertools import combinations
n = int(input())
demo = [i+1 for i in range(n)]

a = [list(map(int,input().split())) for _ in range(n)]
print(list(combinations(demo,len(demo)//2)))