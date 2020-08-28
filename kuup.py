def kuup(jarj):
    if len(jarj) == 0:
        return jarj
    elif len(jarj) == 1:
        return [jarj[0] ** 3]
    else:
        return [jarj[0] ** 3] + kuup(jarj[1:])
    
print(kuup([6, 2, 3, 7]))