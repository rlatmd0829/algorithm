from collections import Counter

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    kind = []

    for a,b in clothes:
        kind.append(b)

    kind = Counter(kind)
    print(kind.values())

solution(clothes)