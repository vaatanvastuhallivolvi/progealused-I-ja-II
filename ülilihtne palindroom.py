fail = open("sõnad.txt", encoding="UTF-8")
kuulilennuteetunneliluuk = []

for rida in fail:
    kuulilennuteetunneliluuk += [rida.strip()]
    
fail.close()

for el in kuulilennuteetunneliluuk:
    if el[::] == el[::-1]:
        print(el)
