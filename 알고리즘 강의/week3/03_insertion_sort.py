input = [4, 6, 2, 9, 1]


def insertion_sort(array): # O(N^2) 버블정렬과 선택정렬과 다른것은 break문이 있기 때문에 최선의 경우는 O(N)이기 때문에 좀더 효율적이다.
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i- j -1] > array[i-j]:
                array[i- j -1], array[i-j] = array[i-j], array[i- j -1]
            else:
                break
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!