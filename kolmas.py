def maiustuste_kogused(lao_seis):
    ladu = {}
    for rida in lao_seis:
        (võti, väärtus) = rida.split()
        ladu[võti] = väärtus
    return ladu

maiustused = ("šokolaad 50", "marmelaad 40", "kohuke 100", "kompvek 1050", "halvaa 250",
              "rullbiskviit 700", "rosin 4000")

nõudmine = input("Palun sisestage soovitud maiustuse nimetus: ")

print("Maiustust " + str(nõudmine) + " on alles " +
str(maiustuste_kogused(maiustused)[nõudmine]) + ".")