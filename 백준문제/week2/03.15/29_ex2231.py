a = int(input()) # a의 가장 작은 생성자를 구하시오

result = 0
for i in range(a): # 0 부터 a까지 for문 돌음

    result = i # 이전값 출력하기 위해서 저장해둠
    str_i = str(i) # 자릿수를 쉽게 더하기 위해 문자열로 변환
    for j in str_i:
        i += int(j) # ex) i = 198 + 1 + 9 + 8

    if i == a: # i 값이 입력값과 똑같다면
        print(result) # 저장해둔 값 출력
        break
else: # for에서 break가 한번도 안걸렸다면 생성자가 없는거기 떄문에 0출력
    print(0) 
    



