input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")  # ord는 문자를 숫자로 바꿔준다.
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index] # abcde.....z 순으로 넣기때문에 기존 문자열에 순서를 보장해주지 않는다.
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index+ord("a")))

    for char in string:  # not_repeating_character_array안에 있는 순서는 기존 문자열에 순서를 보장해주고 있지 않기 때문에
        if char in not_repeating_character_array: 
            return char # 기존 문자열 순서로 for문을 돌려서 나오면 바로 리턴



result = find_not_repeating_character(input)
print(result)