# def solution(n):
#     answer = ''
#     while n>0:
#         n -= 1
#         answer = '124'[n%3] + answer
#         n = n // 3
#     return answer

# 1 2 4 11 12 14
# 1 2 3  4  5  6

# 1,2,3 인 경우 1,2,4로 되고
# 두자리인 경우도 결국 앞에 1,2,4 가 붙기 때문에 

stack = [2,3,4,5]
print(stack[-1])