def protsent(arv1, arv2):
    arv = round((arv2 - arv1) / arv1 * 100, 2)
    return arv

faili_nimi = input("Palun sisestage faili nimi: ")

valmis2 = []
with open(faili_nimi, encoding = "UTF-8") as fail: 
    valmis = fail.read().splitlines()
    for rida in valmis:
        valmis2.append(float(rida))
        
fail.close()
    
igapäev = []
for i in range(len(valmis2)):
    if i + 1 < len(valmis2):
        kakspäeva = protsent(valmis2[i], valmis2[i + 1])
        igapäev.append(kakspäeva)
    else:
        pass
    
igapäev2 = list(map("{}%".format, igapäev))
    
print(*igapäev2, sep = "\n")

maks = max(igapäev)

print("Kõige suurem testide arvu tõus eelmise päevaga võrreldes oli " + str(maks) + "%.")

tõusev = 0
langev = 0
for i in range(len(valmis2)):
    if i + 1 < len(valmis2):
        if valmis2[i] < valmis2[i + 1]:
            tõusev += 1
        else:
            langev += 1
    else:
        pass

print("Tehtud testide arv kasvas " + str(tõusev) + ". ja vähenes " + str(langev) + ". päeval.")