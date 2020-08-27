from math import ceil

a = int(input("Mitu küpsist mahub kandikule laiuses: "))
b = int(input("Mitu küpsist mahub kandikule pikkuses: "))
c = int(input("Mitu kihti on tordil: "))
d = int(input("Mitu küpsist on ühes pakis: "))

pakkide_arv =  ceil(a * b * c / d)
lause_osa = " küpsisepakki tuleb tordi jaoks osta."
minepoodi = str(pakkide_arv)+lause_osa

print(minepoodi)
