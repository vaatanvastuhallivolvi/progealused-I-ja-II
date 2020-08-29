Failis on loomade nimetused, aga sama nimetus võib korduda. Näiteks võib failisisu olla järgmine:
karu
karu
rebane
rebane
rebane
jänes
hunt
siil
Koostada funktsioon loomad, mis võtab argumendiks failinime ja tagastab hulga, kus on kõikide
loomade nimetused, mis on failis. Seejärel kirjutada põhiprogramm, mis kasutab funktsiooni loomad ja
väljastab loomade nimetused ekraanile üksteise alla (järjekord ei ole oluline). Põhiprogramm leiab ja
väljastab ekraanile, mitme erineva looma nimetused failis olid.
Näide programmi tööst:
>>> %Run loomad.py
hunt
rebane
siil
jänes
karu
Erinevaid loomi oli kokku 5.
--------------------------------------------
def loomad(faili_nimi): #pylint: disable = unused-argument
    sõnad = set(open(fail, encoding = "UTF-8").read().split())
    return sõnad

fail = input("Palun sisestage faili nimi: ")

nimekiri = loomad(fail)
pikkus = len(nimekiri)
    
print(*nimekiri, sep = "\n")
print("Erinevaid loomi on kokku " + str(pikkus) + ".")
