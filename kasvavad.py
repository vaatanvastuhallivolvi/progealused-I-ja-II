def on_kasvav(rida):
    if len(rida) < 1:
        return 0
    eelmine = rida[0]
    for el in rida[1:]:
        if el <= eelmine:
            return 0
        eelmine = el
    return 1
            
jarjend_ruudus = [[0, 5, 4, 1], [3, 4]]

kasvavaid = 0
for arvud in jarjend_ruudus:
    kasvavaid += on_kasvav(arvud)
    
print("Kasvavaid ridu on " + str(kasvavaid) + ".")