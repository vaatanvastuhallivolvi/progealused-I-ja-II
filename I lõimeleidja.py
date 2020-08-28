def lõimede_pikkus(vaip, lõimed):
    return round(lõimed * (float(vaip) * 1.2 + 0.5), 2)

lendav = input('Palun sisestage otsitava faili pealkiri "Lendavad_vaibad.txt": ')
pikemad = int(input("Palun sisestage kõrvuti olevate lõimede arv 5-meetriste ja pikemate vaipade puhul: "))
lühemad = int(input("Palun sisestage kõrvuti olevate lõimede arv vaipade puhul, mis on lühemad kui 5 meetrit: "))

with open(lendav, encoding = "UTF-8") as fail: 
    vaibad = fail.read().splitlines()

lõimed2 = []
for el in vaibad:
    if float(el) >= 5:
        vaibakas = lõimede_pikkus(el, pikemad)
    else:
        vaibakas = lõimede_pikkus(el, lühemad)
    print(vaibakas)
    lõimed2 += [vaibakas]
    
summa = 0
for vaibakas in lõimed2:
    summa += vaibakas

summa = round(summa, 2)
print("Kõigi vaipade peale läheb vaja " + str(summa) + " meetrit lõimeniiti.")
