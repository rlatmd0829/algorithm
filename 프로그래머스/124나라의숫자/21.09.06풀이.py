# 생각을 못하겠다 답지 참고
def solution(n):
    answer = ''
    demo = [1,2,4]
    while n > 0:
        n -= 1
        answer = str(demo[n%3]) + answer
        n = n // 3

    return answer
    
    