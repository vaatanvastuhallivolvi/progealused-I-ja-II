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