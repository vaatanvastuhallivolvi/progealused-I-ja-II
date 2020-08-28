def pikim_pikkus(järjend):
    pikkus = len(järjend)
    for el in järjend:
        if isinstance(el, list) == True:
            if pikim_pikkus(el) > pikkus:
                pikkus = pikim_pikkus(el)
    return pikkus