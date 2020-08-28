def yhisosa(järjend1, järjend2):
    ühine = []
    for sõne in järjend1:
        if sõne in järjend2 and sõne not in ühine:
            ühine.append(sõne)
    return ühine