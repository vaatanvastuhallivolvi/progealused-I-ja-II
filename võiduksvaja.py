def nurkademanguks_vaja(tabel):
    nurgad = []
    for i in range(1):
        if tabel[0][0] != "X":
            nurgad.append(tabel[0][0])
        if tabel[0][-1] != "X":
            nurgad.append(tabel[0][-1])
        if tabel[-1][-1] != "X":
            nurgad.append(tabel[-1][-1])
        if tabel[-1][0] != "X":
            nurgad.append(tabel[-1][0])
    return nurgad
            
def diagonaalidemanguks_vaja(tabel):
    diagonaal = []
    for i in range(5):
        if tabel[i][i] != "X":
            diagonaal.append(tabel[i][i])
    for i in range(1):
        if tabel[4][0] != "X":
            diagonaal.append(tabel[4][0])
        if tabel[3][1] != "X":
            diagonaal.append(tabel[3][1])
        if tabel[1][3] != "X":
            diagonaal.append(tabel[1][3])
        if tabel[0][4] != "X":
            diagonaal.append(tabel[0][4])
    return diagonaal

def taismanguks_vaja(tabel):
    jaagupott = []
    for rida in tabel:
        for arv in rida:
            if arv != "X":
                jaagupott.append(arv)         
    return jaagupott