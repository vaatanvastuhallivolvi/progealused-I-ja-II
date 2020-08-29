def loomad(faili_nimi): #pylint: disable = unused-argument
    sõnad = set(open(fail, encoding = "UTF-8").read().split())
    return sõnad

fail = input("Palun sisestage faili nimi: ")

nimekiri = loomad(fail)
pikkus = len(nimekiri)
    
print(*nimekiri, sep = "\n")
print("Erinevaid loomi on kokku " + str(pikkus) + ".")