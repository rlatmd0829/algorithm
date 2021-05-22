
N=7

array = [22,35,11,38,33,14,12,30,18,31,13,4,20,26,2,9,27,19,36,15]

for i in range(0,len(array)-2):
    #print(i,i+1,i+2)
    total =0
    total=abs(array[i]-array[i+1]) + abs(array[i+1]-array[i+2]) + abs(array[i+2]-array[i])
    #print(array[i]-array[i+1])
    print(total)
