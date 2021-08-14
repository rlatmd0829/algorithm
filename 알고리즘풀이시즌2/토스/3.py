def solution(amountText):
    
    list(amountText)
    if amountText[0] == ',' or amountText[-1] == ',':
        return False
    answer = []
    for i in amountText:
        if 48 <= ord(i) <=57 or i == ',':
            answer.append(i)
        else:
            return False
    
    result = ''.join(answer)
    result = result.split(',')
    
    for i in range(len(result)):
        if len(result) == 1:
            z = list(result[0])
            
            if z[0] == '0':
                return False
        else:
            print(len(result[0]))
            if i >= 1 and 3 != len(result[i]) or len(result[0]) > 3:
                return False
            if i >= 1 and result[0][0] == '0':
                return False
    return True
print(solution("0"))