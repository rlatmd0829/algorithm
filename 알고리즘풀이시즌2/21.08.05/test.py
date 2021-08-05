from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement

lis = [1,2,3]

print(list(permutations(lis, 2))) # 순열 : 순서가 있는 조합 ex) (1,2) 와 (2,1) 을 다른거라 본다. 중복허용 X
print(list(combinations(lis, 2))) # 조합 : 순서를 고려 안해서 ex) (1,2) 와 (2,1)을 같은거라 봐서 1개만 출력된다. 중복 허용 X
print(list(product(lis, repeat=2))) # 중복순열, 순열에서 중복 허용
print(list(combinations_with_replacement(lis, 2))) # 중복조합 자신과 같은값만 중복허용 ex) (2,2)는 되는데 (2,1)은 (1,2)가 있어서 안된다.