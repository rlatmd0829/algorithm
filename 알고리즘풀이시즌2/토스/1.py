import math
def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액 (공급가액 + 부가가치세 + 봉사료)
    # taxFreeAmount : 비과세금액 부가가치세가 부과되지 않는 금액
    # serviceFee : 봉사료 (숙박업 등 봉사료가 존재하는 곳만 해당)
    # 공급대가 - 비과세금 = 1원 이면 부가가치세는 0원
    answer = 0
    result = 0
    if taxFreeAmount != 0:
        answer = orderAmount - taxFreeAmount
    
    else:
        answer = orderAmount
    answer = math.ceil(answer / 10)
    eork = orderAmount - answer
    if serviceFee != 0:
        answer = orderAmount - serviceFee
        if answer - taxFreeAmount == 1:
            return 0
    
    
    
    return answer