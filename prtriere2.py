a = int(input("a = "))
b = int(input("b = "))

# Transformam variabilele integer in liste cu stringuri
lsta = list(str(a)) 
lstb = list(str(b))

# Afisam listele
print(lsta)
print(lstb)

# Parcurgem lista a si verificam daca elementele din a sunt in b
rezult = True
for i in range(0, len(lsta)):
    if not (lsta[i] in lstb) :
        rezult = False
        break

# Parcurgem lista b si verificam daca elementele din b sunt in a
for i in range(0, len(lstb)):
    if not (lstb[i] in lsta) :
        rezult = False
        break

# Afisam rezultatul, daca numerele sunt prietene, afisaza "True"
# Daca nu sunt prietene, afiseaza "False" 
print(rezult)  
