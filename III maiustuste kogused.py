Koostada funktsioon maiustuste_kogused, mis võtab argumendiks enniku, mille elemendid on
maiustuste nimetused koos kogusega sõnena. Näiteks võib ennik olla järgnev:
('šokolaad 5', 'marmelaad 4', 'kohuke 10', 'kompvek 15')
Funktsioon tagastab sõnastiku, mille võtmeteks on maiustuste nimetused ja väärtusteks kogused.
Seejärel kirjutada põhiprogramm, mis küsib kasutajalt maiustuse nimetust (võib eeldada, et sisestatud
maiustus on sõnastikus olemas), rakendab funktsiooni maiustuste_kogused ning väljastab
ekraanile, mitu sellist maiustust alles on.
Näide funktsiooni rakendamisest:
>>> maiustuste_kogused(('šokolaad 5', 'marmelaad 4', 'kohuke 10', 'kompvek
15'))
{'šokolaad': '5', 'marmelaad': '4', 'kohuke': '10', 'kompvek': '15'}
Näide programmi tööst:
>>> %Run 'sõnastik.py'
Sisestage maiustuse nimetus: kohuke
Maiustust kohuke on alles 10.
------------------------------------------------
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
