def netopalk(brutopalk):
    tulumaks = (brutopalk - 170) * 0.2
    return round(brutopalk - tulumaks, 2)

netoks_isa = int(input("Palun sisestage isa brutopalk täisarvuna: "))
netoks_ema = int(input("Palun sisestage ema brutopalk täisarvuna: "))
lapsed = int(input("Palun sisestage alaealiste laste arv: "))

isa_sissetulek = netopalk(netoks_isa)
ema_sissetulek = netopalk(netoks_ema)
lastetoetus = lapsed * 50

fin_sissetulek = round(isa_sissetulek + ema_sissetulek + lastetoetus, 2)

if str(fin_sissetulek)[-2:] == ".0":
    lõpp = str(fin_sissetulek)[:-2]
else:
    lõpp = fin_sissetulek

print("Pere kuusissetulek on " + str(lõpp) + " krooni.")
