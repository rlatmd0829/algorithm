import string
import math
import sys
sys.setrecursionlimit(10**6)
def solution(n, k):
    answer = 0
    
    def pri(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) +1):
            if n % i == 0:
                return False
        return True
        
    def change(n, k):
        a = []
        while n >= k:
            a.append(n % k)
            n = n // k
        a.append(n)
        
        return a[::-1]
        
    result = change(n, k)
    
    text = ''
    for i in result:
        if text:
            if i == 0:
                print(text)
                if pri(int(text)):
                    
                    answer += 1
                text = ''
            else:
                text += str(i)
        else:
            if i == 0:
                continue
            text += str(i)
    
    if text:
        if pri(int(text)):
            answer += 1
    
    return answer