def recursive(lotto, n, lst):
    if len(lst) == 6:
        print(' '.join(map(str,lst)))
        return
    if n == len(lotto):
        return
    recursive(lotto, n+1, lst + [lotto[n]])
    recursive(lotto, n+1, lst)

while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    n = lotto.pop(0)
    recursive(lotto, 0, [])
    print()