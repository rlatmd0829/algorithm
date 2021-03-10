a = input()
b = input()

a = int(a)
b = int(b)

q1 = int(b % 10) 
q2 = int((b / 10)) % 10 
q3 = int(int((b / 10)) / 10) 

print(a*q1)
print(a*q2)
print(a*q3)
print(a*b)