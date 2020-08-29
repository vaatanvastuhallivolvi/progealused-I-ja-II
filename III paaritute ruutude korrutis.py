Koostada rekursiivne funktsioon paaritute_ruutude_korrutis, mis võtab argumendiks ühe
positiivse täisarvu ja tagastab kõikide positiivsete paaritute täisarvude ruutude korrutise, mis on
väiksemad või võrdsed argumendiga. Kontrollitakse vaid funktsiooni definitsiooni, programmis seda
rakendama ei pea.
Näited programmi tööst:
>>> paaritute_ruutude_korrutis(5)
35
>>> paaritute_ruutude_korrutis(4)
10
--------------------------------------------
def paaritute_ruutude_korrutis(n):
    if n == 1:
        return 1
    elif n % 2 != 0 and n > 0:
        return n * n * paaritute_ruutude_korrutis(n - 2)
    else:
        return paaritute_ruutude_korrutis(n - 1)
