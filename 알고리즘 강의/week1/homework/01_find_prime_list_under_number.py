input = 20

array = []



def find_prime_list_under_number(number):
    for index in range(2,number+1): #range는 2~number+1 미만 까지 하겠다는 소리,  range는 미만임 조심하기
        for arr in array: # <소수구하기 문제 꿀팁1> 2 ~ index-1 범위까지 전부 해볼 필요 없이 소수만 나눠보면 된다. 왜냐하면 2또는 3같은 소수로 나눠지면 4,6 같은 것은 무조건 나눠지기 때문에 해볼 필요없다.
            if index % arr == 0 and arr*arr <= index:
                break
        else:
            array.append(index)

    return array

#<소수구하기 문제 꿀팁2> N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
#수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘중 하나는 반드시 N의 제곱근 이하이다.
#즉 범위가 20이라면 20의 제곱근까지만 해보면 된다.

result = find_prime_list_under_number(input)
print(result)