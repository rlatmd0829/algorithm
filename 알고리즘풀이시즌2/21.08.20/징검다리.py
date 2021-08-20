# 시간초과 이분탐색으로 해야하는데 접근법을 모르겠다.

from itertools import combinations
import copy

def solution(distance, rocks, n):
    com = list(combinations(rocks,n))
    maxx = 0
    for x,y in com:
        result = []
        temp = copy.copy(rocks)
        temp.remove(x)
        temp.remove(y)
        temp.sort()
        for i in range(len(temp)+1):
            if i == 0:
                result.append(temp[i])
            elif i == len(temp):
                result.append(distance - temp[i-1])
            else:
                result.append(temp[i] - temp[i-1])
                
        maxx = max(maxx,min(result))
    return maxx