from itertools import permutations
from itertools import combinations
items = [6,10,2]

permute = list(permutations(items, len(items)))
#print(permute)
list_permute = []
for i in permute:
    #print(i)
    #print(map(str,i))
    #print(''.join(map(str,i)))
    list_permute.append(''.join(map(str,i)))

print(max(list_permute))
#print(list_permute)

#print(list(combinations(items, len(items))))

#####################################

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

### ['6','10','2'] => ['666','101010','222']
### 문자열 정렬은 인덱스 맨 앞에값에 아스키값을 비교해 정렬을 해준다고 한다 (같을경우 다음 인덱스도 비교)
### reverse=True 이므로 ['6','2','10']으로 정렬 된다.

stack = [2,3,4,5]
print(stack[-1])