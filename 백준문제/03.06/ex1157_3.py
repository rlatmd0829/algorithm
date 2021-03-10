s = input()
alphabet = [0] * 26
for i in s:
    if ord(i) < 97:
        a = ord(i) - ord("A")
        alphabet[a] += 1
    else:
        a = ord(i) - ord("a")
        alphabet[a] += 1

max = alphabet[0]
temp =0
for i in range(0,26):
    if max < alphabet[i]:
        max = alphabet[i]
        temp =i

cnt=0
for i in alphabet:
    if max == i:
        cnt +=1
    if cnt ==2:
        print("?")
        break
else:
    print(chr(temp + ord("A")))

#####################################

word = input().upper()  # word = mississipi / baaa

word_list = list(set(word)) # word_list = [m, i, s, p] / [b, a]
cnt = []

for i in word_list: # i = m, i, s, p / b, a
    count = word.count(i) # count는 요소의 개수를 세준다.
    cnt.append(count) # cnt = [4,4,1,1] / [1,3]

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))]) # index는 리스트에 그 값이 있으면 위치를 반환해준다.