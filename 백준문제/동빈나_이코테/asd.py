
def solution(s):
    numbers = [["zero" ,'0'], ["one",'1'], ["two",'2'], ["three",'3'], ["four",'4'], ["five",'5'], ["six",'6'], ["seven",'7'], ["eight",'8'], ["nine",'9']]
    number = ""
    answer = []
    for i in s:
        if ord(i) >= 48 and ord(i) <= 57:
            answer.append(i)
        else:
            number += i
            if len(number) >= 3:
                for j in numbers:
                    print(j[0])
                    print(number)
                    if number == j[0]:
                        answer.append(j[1])
                        number = ""
                        break
    
    s = "".join(answer)     
    return int(s)

print(solution("one4seveneight"))
