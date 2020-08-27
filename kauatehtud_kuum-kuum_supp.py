a = int(input("Kui kõrge on supi algtemperatuur: "))
t = int(input("Kui kõrge on toatemperatuur: "))

k = 0.19
jahtuv_supp = a
minut = 0
while minut < 10:
    jahtuv_supp = jahtuv_supp - (jahtuv_supp - t) * k
    minut = minut + 1

print("Supi temperatuur " + str(minut) + " minuti pärast on: " + str(round(jahtuv_supp)) + " kraadi" + ".")