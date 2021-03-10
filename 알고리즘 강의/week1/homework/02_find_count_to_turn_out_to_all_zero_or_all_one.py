input = "10001010001"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0  # 전부 0으로 변환시키는 경우에 최소횟수
    count_to_all_one = 0  # 전부 1로 변환시키는 경우에 최소횟수
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1
    for i in range(len(string)-1):
        if string[i] != string[i+1]:  # 1에서 0 혹은 0에서 1로 변했다는 소리
            if string[i+1] == '0':
                count_to_all_one += 1
            if string[i+1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one,count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
