fail = open("sõnad.txt", encoding="UTF-8")
sõnad = []

for rida in fail:
    sõnad += [rida.strip()]
    
fail.close()

for el in sõnad:
    if el[::] == el[::-1]:
        print(el)