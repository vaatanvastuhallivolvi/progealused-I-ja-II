Failis on kino istumiskohtade plaan, kus igas reas on 10 kohta ja saalis on 10 rida. Kino
istumiskohtade broneering on esitatud failis nii, et "K" tähistab kohta, mis on kinni ja
"V" kohta, mis on vaba. Esimene rida failis vastab saali esimesele reale.
Koostada funktsioon failist_jarjendisse, mis
 võtab argumendiks failinime,
 tagastab kahemõõtmelise järjendi kino broneeringute kohta.
Koostada funktsioon on_vaba, mis
 võtab argumentideks rea, istekoha ja kahemõõtmelise järjendi,
 tagastab tõeväärtuse (True või False) vastavalt sellele, kas antud koht on
vaba.
Koostada programm, mis
 küsib kasutaja käest failinime,
 loeb failist andmed järjendisse kasutades funktsiooni failist_jarjendisse,
 küsib kasutaja käest, millisesse ritta ta soovib istuda (täisarv 1-10),
 küsib kasutaja käest, millisele kohale ta soovib istuda (täisarv 1-10),
 väljastab kasutajale, kas koht oli vaba või kinni, kasutades funktsiooni on_vaba.
Arvestada tuleb, et programmi kasutaja loendab ridu ja kohti alates ühest.
Näited on järgmisel leheküljel.
 
Näide faili kohta:
kino.txt
K K K K V K K V K K
K K V K V K K K K V
V K K K K K V V K K
K K K K V K K V K K
K K V V V V K V K K
V K K K K K K K K V
K V K K V K V V K K
K K K K V K K V K K
K V K K V K K V K K
K K V K V K K V K K
Näited funktsioonide kohta:
>>> failist_jarjendisse("kino.txt")
[['K', 'K', 'K', 'K', 'V', 'K', 'K', 'V', 'K', 'K'], ['K', 'K',
'V', 'K', 'V', 'K', 'K', 'K', 'K', 'V'], ['V', 'K', 'K', 'K',
'K', 'K', 'V', 'V', 'K', 'K'], ['K', 'K', 'K', 'K', 'V', 'K',
'K', 'V', 'K', 'K'], ['K', 'K', 'V', 'V', 'V', 'V', 'K', 'V',
'K', 'K'], ['V', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'V'],
['K', 'V', 'K', 'K', 'V', 'K', 'V', 'V', 'K', 'K'], ['K', 'K',
'K', 'K', 'V', 'K', 'K', 'V', 'K', 'K'], ['K', 'V', 'K', 'K',
'V', 'K', 'K', 'V', 'K', 'K'], ['K', 'K', 'V', 'K', 'V', 'K',
'K', 'V', 'K', 'K']]
>>> on_vaba(1, 3, failist_jarjendisse("kino.txt"))
False
>>> on_vaba(10, 3, failist_jarjendisse("kino.txt"))
True 
------------------------------------------
import numpy as np

def failist_järjendisse(faili_nimi):
    broneering = []
    fail = open(faili_nimi)
    for rida in fail:
        rea_järjend = []
        osad = rida.split()
        for osa in osad:
            rea_järjend.append(osa)
        broneering.append(rea_järjend)
    fail.close()
    return broneering

def on_vaba(rida, koht, järjend):
    if järjend[rida - 1][koht - 1] == "V":
        return "Teie koht on vaba."
    else:
        return "Teie koht on kinni."
    
failikas = input("Palun sisestage faili nimi: ")
järjend = failist_järjendisse(failikas)

kohad = np.array(järjend)

vaba = np.argwhere(kohad == "V")
print("Kuvan vabad kohad. Esimene number märgib rida, teine kohta: " + str(vaba + 1) + ".")

a = input("Millisesse ritta Te soovite istuda, read 1-10: ")
b = input("Millisele kohale Te soovite istuda, kohad 1-10: ")

print(on_vaba(int(a), int(b), järjend))
