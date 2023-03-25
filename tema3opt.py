# EXERCITII OPTIONALE

# 1. Ne imaginam o echipa de fotbal.
# a. Declara o lista cu 5 jucatori (numele lor) care sunt pe teren: lista_jucatori_teren.
lista_jucatori_teren = ['teren1', 'teren2', 'teren3', 'teren4', 'teren5']

# b. Declara o lista cu 5 jucatori (numele lor) care sunt de rezerva: lista_jucatori_rezerva.
lista_jucatori_rezerva = ['rezerva1', 'rezerva2', 'rezerva3', 'rezerva4', 'rezerva5']

# c. Declara o lista goala cu jucatori care sunt scosi de pe teren: lista_jucatori_scosi.
lista_jucatori_scosi =[]
# d. Declara constanta SCHIMBARI_MAXIME = 3.
SCHIMBARI_MAXIME = 3

# e. Declara o variabila schimbari_efectuate. (Joaca-te cu valori diferite sa vezi cum curg datele prin cod).
schimbari_efectuate = int(input('schimbari efectuate'))
schimbari_ramase = SCHIMBARI_MAXIME-schimbari_efectuate >= 0
print(f'schimbari ramase{schimbari_ramase}')
print(f'schimbari efectuate{schimbari_efectuate}')
# f. Citeste numele a doi jucatori de la tastatura, salveaza-le numele in variabilele x si y.
x= print(input('jucator 1'))
y= print(input('jucator 2'))
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
#   Efectuam urmatoarea schimbare daca jucatorul y e in lista de rezerve si nu exista in lista de teren:
        # Stergem jucatorul x din lista de teren si il adaugam in lista de jucatori scosi
        # Adaugam jucatorul y in lista de jucatori pe teren si il scoatem din lista de jucatori de rezerva
        # Crestem numarul de schimbari_efectuate (hint: operator de atribuire)
        # Afisam pe ecran: a intrat y, a iesit x. Mai aveti z schimbari (inlocuiti x, y si z cu numele variabilelor voastre)
#   Daca jucatorul y este pe teren deja:
        # Afisam ‘nu se poate efectua schimbarea deoarece jucatorul y e deja pe teren teren’
        # Afisam si nr schimbari: ‘mai aveti z schimbari’.


if x == lista_jucatori_teren and schimbari_ramase< 3:
    if y==lista_jucatori_rezerva and y != lista_jucatori_rezerva:
        lista_jucatori_teren.remove(x)
        lista_jucatori_scosi.append(x)
        lista_jucatori_teren.append(y)
        lista_jucatori_rezerva.remove(y)
        schimbari_efectuate=2
        print(f'a intrat {y}, a iesit {x}. Mai aveti {schimbari_ramase} schimbari')
    else:
        print(f'nu se poate efectua schimbarea deoarece jucatorul {y} e deja pe teren teren'
              f'mai aveti {schimbari_ramase} schimbari')
else:
    print(lista_jucatori_teren)


