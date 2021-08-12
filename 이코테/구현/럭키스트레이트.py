n = list(input())
leng = len(n)
answer1 = 0
answer2 = 0
for i in range(leng):
    if i < leng//2:
        answer1 += int(n[i])
    else:
        answer2 += int(n[i])

if answer1 == answer2:
    print("LUCKY")
else:
    print("READY")
