
numbers1 = set(range(1,10001))
numbers2 = set()
def qqq(a):
    sum=0
    temp = a
    while a>0:
        q1= a%10
        a = int(a/10)
        sum += q1
    b = sum+temp
    numbers2.add(b)
    

for i in range(1,10001):
    qqq(i)
        

self_numbers = numbers1 - numbers2
for i in sorted(self_numbers):
    print(i)