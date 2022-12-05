def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    return sum

n = int(input("n = "))
m = int(input("m (suma) = "))
multimea = range(0, n+1)

print("Suma m = ", m)
print("Multimea: ", multimea)

k=0
for i in range(0, len(multimea)):
    if getSum(multimea[i]) == m:
        k+=1
print("Cate numere din aceasta multime suma cifrelor fiecarui numar fiind egal cu m: ", k)
