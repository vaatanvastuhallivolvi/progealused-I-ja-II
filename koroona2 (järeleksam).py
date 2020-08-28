Terviseameti lehel on koroonaviiruse testide avaandmed, mida igaüks saab vabalt vaadata. Selle info põhjal
on loodud tekstifail, kus on 22.-31. märtsini tehtud testide arvud eraldi ridadel (igal real on ühe päeva testide
arv). Ülesandeks on kirjutada programm, mis leiab, mitu protsenti muutus tehtud testide arv eelmise päevaga
võrreldes, kui suur oli suurim kasv, mitmel päeval testide arv kasvas ja mitmel kahanes.
Koosta funktsioon protsent, mis
● võtab argumentideks kaks täisarvu,
● tagastab, mitu protsenti kasvas või kahanes tehtud testide arv eelmise päevaga võrreldes (ümardatuna
sajandikeni).
Muutuse leidmiseks saab kasutada valemit (arv2 - arv1) / arv1 * 100
Koosta programm, mis
● küsib kasutajalt
○ failinime (failis on eraldi ridadel iga päeva testide arvud),
● loeb failist tehtud testide arvud (fail tuleb ise luua),
● leiab funktsiooni protsent rakendades kõikide päevade kohta, mitu protsenti suurenes või vähenes
tehtud testide arv eelmise päevaga võrreldes (alustatakse muutusest esimese ja teise päeva vahel),
● väljastab leitud protsendid ekraanile,
● leiab ja väljastab ekraanile, kui suur oli kõige suurem testide arvu kasv protsentides eelmise päevaga
võrreldes (vastus ümardada sajandikeni),
● leiab ja väljastab ekraanile, mitmel päeval tehtud testide arv eelmise päevaga võrreldes kasvas ja
mitmel päeval kahanes.
Näited funktsiooni protsent rakendamisest:
>>> protsent(160, 495)
209.38
>>> protsent(1403, 1047)
-25.37
Näide programmi tööst (kasutaja sisestus on kaldkirjas):
Faili andmed.txt sisu:
160
495
1403
1047
1139
1253
1035
851
1153
1977
>>> %Run 'viirusetestide-analüüs.py'
Sisestage failinimi: andmed.txt
209.38%
183.43%
-25.37%
8.79%
10.01%
-17.4%
-17.78%
35.49%
71.47%
Kõige suurem testide arvu tõus eelmise päevaga võrreldes oli 209.38%.
Tehtud testide arv kasvas 6 ja vähenes 3 päeval.
----------------------------------------------------
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
