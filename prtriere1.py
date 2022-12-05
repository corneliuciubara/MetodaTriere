n = int(input("n = "))
m = int(input("m = "))
i = int(input("i = "))
k = int(input("k = "))
def sumacifrelor(num):
    s = 0
    while (num!=0):
        s = s + num%10
        num = num/10
    return s

def solutieposibila(num):
    if (sumacifrelor(num)==m):
        return True
    else:
        return False

def prelucraresolutie(num, k):
    print(num)
    k+=1

print("n = ", n)
print("m = ", m)
for i in range(1, n):
    if (solutieposibila(i)):
        prelucraresolutie(i, k)
    if k == 0:
        print("Nu exista")
