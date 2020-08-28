algus = int(input("Kui kõrge on supi algtemperatuur: "))
tuba = int(input("Kui kõrge on toatemperatuur: "))

kordaja = 0.19
jahtuv_supp = algus
minut = 0
while minut < 10:
    jahtuv_supp = jahtuv_supp - (jahtuv_supp - tuba) * kordaja
    minut = minut + 1

print("Supi temperatuur " + str(minut) + " minuti pärast on: " + str(round(jahtuv_supp)) + " kraadi" + ".")
