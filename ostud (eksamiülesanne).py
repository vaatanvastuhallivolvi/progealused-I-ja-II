def üks_tellimus(kauba_maksumus, alates):
    if kauba_maksumus >= 20.00 and kauba_maksumus < int(alates):
        return kauba_maksumus + 4.9
    else:
        return kauba_maksumus
    
faili_nimi = input("Palun sisestage õige faili nimi: ")
alates = input("Palun sisestage, millisest summast alates on kojuvedu tasuta: ")
with open(faili_nimi, encoding = "UTF-8") as fail:
    read = fail.read().splitlines()
hinnad = []
for i in read:
    hinnad.append(i)

keskmikud = []
suured = []
for S in hinnad:
    if float(S) < 20.00:
        jääk = round(float(20) - float(S), 3) 
        print("Maksumus " + str(S) + " on liiga väike. Lisage veel kaupu vähemalt " + str(jääk) + " euro eest.")
    elif float(S) >= 20.00 and float(S) < int(alates):
        keskmine = üks_tellimus(float(S), alates)
        keskmikud.append(keskmine)
        print(keskmine)
    elif float(S) >= int(alates):
        suur = üks_tellimus(float(S), alates)
        suured.append(suur)
        print(suur)

lõplik_hind = keskmikud + suured

summa = 0
for tellimus in lõplik_hind:
    summa += tellimus
    
fail.close()
    
summa = round(summa, 3)

print("Täidetud tellimuste kogusumma on " + str(summa) + " eurot.")