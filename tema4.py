# USOR - recomandat
# 1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# TEMA OBLIGATORIE - nivel usor spre mediu
# SETS
# 1. Se dau urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata'}
weekend = {'sambata', 'duminica'}
# a. Incearca sa adaugi in setul zile_sapt, ziua de 'duminica'.
# Ce observi? Scrie intr-un comentariu observatiile tale.
zile_sapt.add('duminica')
print(zile_sapt)
# in SET se pot adauga elemente, dar acestea nu isi pastreaza ordinea

# b. Foloseste un IF si verifica DACA:
# - weekend este un subset al zilelor din saptamana (adica daca elementele din setul weekend se regasesc
# intre elementele din setul zile_sapt)
# - weekend nu este un subset din setul zile_sapt
# Salveaza rezultatul pentru fiecare caz intr-o variabila bool si afiseaz-o intr-un mesaj sugestiv.
if weekend < zile_sapt:
    print(f'Zilele din Weekend fac parte din zilele saptamanii', True)
else:
    print(f'Zilele din Weekend nu fac parte din zilele saptamanii', False)
if weekend.issubset(zile_sapt):
    print(f'Zilele din Weekend fac parte din zilele saptamanii', True)
else:
    print(f'Zilele din Weekend nu fac parte din zilele saptamanii', False)

# c. Afiseaza diferentele intre cele doua seturi (adica elementele care sunt in zile_sapt
# si nu sunt in weekend si invers).
print(weekend.difference(zile_sapt))
# elementele care sunt in set-ul zile_sapt si nu sunt in set-ul weekend
print(zile_sapt.difference(weekend))



# d. Afiseaza intersectia elementelor din cele doua seturi (adica elementele care exista in ambele seturi).

print(weekend.intersection(zile_sapt))

# TUPLES
# 2. Calcularea valorii totale a unui cos de cumparaturi
# Un client a cumparat mai multe articole dintr-un magazin si dorim sa calculam valoarea totala a cosului
# de cumparaturi.
# Citeste de la tastatura numele si pretul pentru trei articole, pe rand.
nume_produs1= input('produs 1')
pret_produs1 = float(input('pret 1'))
nume_produs2 = input('produs 2')
pret_produs2 = float(input('pret 2'))
nume_produs3 = (input('produs 3'))
pret_produs3 = float(input('pret 3'))


# Salveaza numele si pretul pentru fiecare articol intr-un tuplu. (Astfel vei avea trei tupluri).
nume_produs1 = (nume_produs1, pret_produs1)
print(type(nume_produs1))
nume_produs2 = (nume_produs2, pret_produs2)
nume_produs3 = (nume_produs3, pret_produs3)

# Calculeaza pretul total platit de client si afiseaza rezultatul intr-un mesaj sugestiv.
# cumparaturi (produs, pret)
cos_total = nume_produs1[1] + nume_produs2[1] + nume_produs3[1]
print(f'Valoarea totala a cosului este {cos_total}')


# 3. Se dau urmatoarele tupluri care caracterizeaza tipul de forma geometrica si lungimile laturilor sale.
forma_1 = ("Patrat", 5)
forma_2 = ("Dreptunghi", 2, 3)
# Calculeaza perimetrul si aria pentru fiecare forma geometrica
perimetru1= forma_1[1]+forma_1[1] +forma_1[1] +forma_1[1]
print(f'Perimetru {forma_1[0]} este egala cu {perimetru1}')
aria1 = forma_1[1]**2
print(f'Aria {forma_1[0]} este egala cu {aria1}')
perimetru2 = 2*(forma_2[1]+forma_2[2])
aria2 = forma_2[1]*forma_2[2]
print(f'Perimetru {forma_2[0]} este egala cu {perimetru2}')
print(f'Aria {forma_2[0]} este egala cu {aria2}')

# 4. Citeste de la tastatura notele obtinute de un student la cele 4 examene date in sesiune.
nota1= float(input('nota1'))
nota2= float(input('nota2'))
nota3= float(input('nota3'))
nota4= float(input('nota4'))
note = [nota1,nota2,nota3,nota4]

# Salveaza notele intr-un tuplu.
note = tuple(note)
print(note)
media = sum(note)/4
# Calculeaza media studentului la finalul sesiunii.
# Daca media este intre 8-10 (inclusiv capetele de interval), afiseaza-i un mesajul utilizatorului
# si spune-i ca s-a descurcat foarte bine.
# Daca media este intre 5-8, afiseaza-i un mesaj utilizatorului sa se ambitioneze
# sesiunea urmatoare si sa invete mai mult ca sa obtina bursa.
# Daca media este sub 5, afiseaza-i utilizatorului un mesaj in care sa ii spui sa nu isi faca planuri pe vara ca il
# asteapta sesiunea de restante.
if 8<=media<=10:
    print(f'Felicitari, te-ai descurcat foarte bine, ai media {media}')
elif 5<=media<8:
    print(f'daca vei invata mai mult sesiunea urmatoare iei bursa, media ta este {media}')
else:
    print('te astept in sesiunea urmatoare')


# CONDITII REPETITIVE

# 5. Se da lista:
masini = ['Audi', 'Volvo', 'Dacia', 'Mercedes', 'Fiat', 'Trabant', 'Lastun']
# a. Folosind un for si lungimea listei, itereaza prin lista si pentru fiecare element
# afiseaza mesajul 'Masina mea preferata este x', unde x este masina.
for index_masini in range(0,len(masini)):
    print(f' Masina mea preferata este {masini[index_masini]}')


# b. Faceti acelasi lucru folosind un for each.
for masina in masini:
    print(f' Masina mea preferata este {masina}')

# c. Faceti acelasi lucru folosind un while.
i=0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i +=1
else:
    print('am terminat')


# 6. Folosind lista de la exercitiul 5, modifica elementele din lista astfel incat sa fie scrise cu majuscule,
# exceptand primul si ultimul element din lista.
# Printati varianta finala a listei.
for index in range(1,(len(masini)-1)):
    masini[index]= masini[index].upper()
print(masini)

# 7. Folosind lista de la exercitiul 5:
# Vine un cumparator care vrea sa cumpere un Mercedes.
# Itereaza prin lista cu for each, verifica daca masina e mercedes.
# Daca da, afiseaza mesajul
# "Am gasit masina dorita de dumneavoastra" si iesim din ciclu folosind un cuvant cheie care face acest lucru.
# Daca nu, afiseaza "Am gasit masina X. Mai cautam."
masini = ['Audi', 'Volvo', 'Dacia', 'Mercedes', 'Fiat', 'Trabant', 'Lastun']

for masina in masini:
    print(masina)
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam.')


# 8. Folosind lista de la exercitiul 5:
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#   Folositi un cuvant cheie care sa dea skip la ce urmeaza
# In celalalte cazuri, printati mesajul "S-ar putea sa va placa masina x.".

for i in masini:
    if i== 'Trabant' or i== 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {i}')


# 9. Modernizati parcul de masini.
# Creati o lista goala, masini_vechi.
# Iterati prin masini. (lista de la exercitiul 5)
# Cand gasiti Lastun sau Trabant:
#   Salvati aceste masini in masini_vechi.
#   Suprascrieti cu 'Tesla' (in lista initiala de masini)
# Printati: "Modele vechi: x"
# Printati: "Modele noi: y"

masini_vechi=[]
masinii_noi = 'Tesla'

for veche in range(len(masini)):
    if masini[veche] == 'Trabant' or masini[veche]== 'Lastun':
        masini_vechi.append(masini[veche])
        masini[veche]== 'Tesla'
print(f'Modele vechii: {masini_vechi}')
print(f'Modele noi: {masini}')


#10. Avand dictionarul:
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Vine un client cu bugetul de 15 000 euro.
# Prezentati doar masinile care se incadreaza in acest buget:
# Iterati prin dict.items() si acc3esati masina si pretul.
# Printati "Pentru un buget de sub 15 000 euro puteti alege masina x"
buget=15000

for masina, pret in  pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de sub 15 000 euro puteti alege masina {masina} ')
#
#
#
# print('11 ex ')
# 11. Avand lista:
numere = [5, 7, 9, 3, 3, 1, 0, -4, 3]
# Afisati de cate ori apare 3. (! NU aveti voie sa folositi metoda count()!
count=0
for numar in numere:
    if numar==3:
       count+=1
print(f'Numarul 3 apare de {count} ori')

# print('ex 12')
# 12. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin lista si calculati suma numerelor din lista.
# ! NU aveti voie sa folositi functia sum()!
suma = 0
for numar in numere:
    suma+=numar
print(suma)

print('ex 13')
# 13. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin lista si afisati cel mai mare numar.
# ! NU aveti voie sa folositi functia max()!
nr_maxim = numere[0]
for numar in numere:
    if numar>nr_maxim:
        nr_maxim = numar
print(nr_maxim)



print('ex 14')
# 14. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin ea
# - daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa.
# Exemplu: Daca e 3, sa devina -3.
# Afisati noua lista.

for pozitiv in numere:
    if pozitiv>0:
        numere[numere.index(pozitiv)]=-pozitiv
print(numere)



# # TEMA OPTIONALA - DE GRUP (MAY NEED GOOGLE)
print('1op')
# 1. Se dau listele:
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Populati corect listele goale pe baza elementelor din lista alte_numere.
# Afisati cele 4 liste la final.

for x in alte_numere:
    if x % 2 == 0:
        numere_pare.append(x)
    else:
        numere_impare.append(x)
    if x >=0:
        numere_pozitive.append(x)
    else:
        numere_negative.append(x)
print(f'numere pare {numere_pare}')
print(f'numere impare{numere_impare}')
print(f'numere pozitive {numere_pozitive}')
print(f'numere negative{numere_negative}')

print('2op')
# 2. Folosind lista alte_numere de la exercitiul anterior:
# Ordonati lista crescator, fara sa folositi sort.
# Va puteti inspira vizual de aici: https://www.youtube.com/watch?v=lyZQPjUT5B4
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(0, len(alte_numere)-i-1):
        if alte_numere[j]>alte_numere[j+1]:
            temp = alte_numere[j]
            alte_numere[j] = alte_numere[j+1]
            alte_numere[j+1]= temp

print(alte_numere)

# 3. Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# numar_ghicit = None
# Folosind un while:
#   User-ul introduce un numar
#   Programul ii spune:
#   Numarul secret e mai mare
#   Numarul secret e mai mic
#   Ai ghicit.
# Daca utilizatorul a ghicit, while-ul trebuie sa se opreasca!

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None

while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Introdu un numar intrg : '))
    if numar_secret > numar_ghicit:
        print('Numarul secret este mai mare')
    elif numar_secret < numar_ghicit:
        print('Numatul secret este mai mic')
    else:
        print('Ai ghicit')

# 4. Alegeti un numar de la tastatura si generati o piramida, conform exemplului:
# Daca utilizatorul va introduce numarul 7, se va genera/ afisa urmatoarea piramida:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

numar = int(input('Alege un numar natural intreg: '))

for i in range(1, numar+1):
    print(str(i)*i)

# 5.
# tastatura_telefon = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# Iterati prin lista 2d.
# Printati "Cifra curenta este x"
# (HINT: nested for - adica for in for)

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for lista_cifre in tastatura_telefon:
     for cifra in lista_cifre:
         print(f'Cifra curenta este {cifra}')