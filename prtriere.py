valoarea = [1, 5, 10, 25, 50]
nr = [1, 2, 3, 4, 5] 

def solpos(a,b,c,d,e):
    if (nr[0]*a + nr[1]*b + nr[2]*c + nr[3]*d + nr[4]*e == g) and (a+b+c+d+e==n):
        return True
    else:
        return False
def prelucraresol(a,b,c,d,e):
    summin = -1
    sum = valoarea[0]*a+valoarea[1]*b+valoarea[2]*c+valoarea[3]*d+valoarea[4]*e
    if sum >summin
        summin = sum
    if summin==-1:
        summin=sum 
    return print(summin)
n = int(input("Nr de monede din pusculita: "))
g = int(input("Greutatea monedelor din pusculita: "))
for a in range(0, n):
    for b in range(0, n):
        for c in range(0, n):
            for d in range(0, n):
                for e in range(0, n):
                    if solpos(a,b,c,d,e):
                        prelsol(a,b,c,d,e)
