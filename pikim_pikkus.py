def pikim_pikkus(järjend):
    aavopikkuus = len(järjend)
    for el in järjend:
        if isinstance(el, list) == True:
            if pikim_pikkus(el) > aavopikkuus:
                aavopikkuus = pikim_pikkus(el)
    return aavopikkuus
