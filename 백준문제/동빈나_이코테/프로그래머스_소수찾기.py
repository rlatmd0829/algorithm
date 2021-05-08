from itertools import permutations
import math


def is_prime_number(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    answer=[]
    for i in range(1, len(numbers)+1):
        arr = list(permutations(numbers, i)) # for문 첫번째 : [('1',), ('7',)], 두번째 : [('1', '7'), ('7', '1')]
        print(arr)
        for j in range(len(arr)):
            
            num = int(''.join(map(str,arr[j])))
            print(num)
            if is_prime_number(num):
                answer.append(num)
    print(answer)
solution("011")

# new = list("17")
# print(new)
# def solution(numbers):
#     for i in range(2, len(numbers)+1):
#         arr = list(permutations(numbers, i))
#         for j in arr:
#             if len(j) <= len(numbers):
#                 print(j)
#                 new.append(''.join(j))
#                 print(new)
# solution("17")