def solution(n):
    answer = 0
    while n>0:
        if n%5 == 0:
            answer = answer + (n//5)
            break
        n -= 3
        answer += 1
    if n < 0:
        return -1
    else:
        return answer

# 택배를 이용해 총 n개의 옷을 배송하려고 한다.
# 옷 3개 들어가는 상자 5개 들어가는 상자가 있다 배송비를 최소화 하기 위해서 상자를 가장 조금 보내야한다.
# 효율성에 걸려서 if n%5로 나눠질때 n을 -5씩 하는게 아니라 한번에 answer에 결과를 넣어줄 수 있게 answer = answer + (n//5) 써준다.