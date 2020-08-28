def yhisosa(essajärjend, tossajärjend):
    yhine = []
    for sõne in essajärjend:
        if sõne in tossajärjend and sõne not in ühine:
            yhine.append(sõne)
    return yhine
