def paaritute_ruutude_korrutis(n):
    if n == 1:
        return 1
    elif n % 2 != 0 and n > 0:
        return n * n * paaritute_ruutude_korrutis(n - 2)
    else:
        return paaritute_ruutude_korrutis(n - 1)