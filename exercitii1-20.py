# 1. Explica intr-un comentariu ce este o variabila de tip string.
# variabila string este o variabila formate din caractere de la tastatura delimitata de '' sau ""
# 2. Defineste o variabila string, numita descriere si afiseaz-o.
x = 'descriere'
print(x)
# 3. Defineste 3 variabile: oras, strada si nr.
oras= 'Cluj'
stada = 'Rasaritului'
nr = 13
# a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
print('Eu locuiesc in ' + oras + ' pe strada ' + stada + ' la numarul ' + str(nr))

# b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.
print(f'Eu locuiesc in {oras}  pe strada {stada} la numarul {nr}')
# 4. Se da variabila string, nume_complet = 'Pop Maria Ioana'.
nume_complet = 'Pop Maria Ioana'

# a. Afiseaza primul element din string.
print(nume_complet[0])
# b. Afiseaza al doilea prenume.
print(nume_complet.split()[2])
# c. Afiseaza de cate ori apare litera 'a' in nume_complet.
print(nume_complet.count('a'))
# d. Inverseaza string-ul si afiseaza rezultatul.
print(nume_complet[::-1])
# e. Inlocuieste al doilea prenume cu 'Elena'.
print(nume_complet.replace('Ioana', 'Elena'))

# f. Afiseaza caracterele de la indexul 5 la indexul 9 (inclusiv
val1= (nume_complet[4:9])
print(val1)

# g. Afiseaza caracterele de la inceputul string-ului pana la index-ul 8 (inclusiv).
val2 = nume_complet[:8]
print(val2)
# 5. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
culoarea_preferata = input('culoarea preferata')

# a. Determina lungimea inputului citit de la tastatura.
print(culoarea_preferata.__len__())
# b. Determina tipul inputului citit de la tastatura.
print(type(culoarea_preferata))
# c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
print(culoarea_preferata.upper())
# d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
# Afiseaza rezultatul.
print(culoarea_preferata.capitalize())

# 6. Se da variabila my_var = '1234' . Verifica daca my_var este compus doar din numere.
my_var = '1234'
my_var1 = 1234

assert my_var.isnumeric()

print("da")

# 7. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
anotimp = 'primavara'
print(anotimp.count('vara'))
assert anotimp.count('vara') == True
print('avem vara in primavara')

# 8. Citeste de la tastatura numarul de zile ramase pana la vacanta.
# Verifica, folosind assert, daca numarul de zile este mai mare de 7 zile.
vacanta_come = int(input('zile ramase pana la vacanta'))
assert vacanta_come > 7
print('vacanta vine in mai mult de o sapatamana')

# 9. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
pret_cos_cumparaturi = float(input('cosul costa'))
print(pret_cos_cumparaturi-(pret_cos_cumparaturi*25/100))
#
#
# 10. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
# Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'
lista= zile_sapt.split(',')
print(lista)
print(type(lista))
    

# ???11. Se citeste de la tastatura 2 string-uri. Verifica daca al doilea string se gaseste in primul.
# str1 = print(input('string1'))
# str2 = print(input('string2'))
# assert str1>= str2
# print('str 2 este inclus in str 1')
#
# 12. Scrie un program care solicita utilizatorului sa introduca varsta sa
# și returneaza un mesaj personalizat, in funcție de varsta introdusa.
# Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
# mesajul "Esti major si poti vota".
# # In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
varsta = float(input('introdu varsta ta'))
if varsta>= 18:
    print("Esti major si poti vota")
else:
    print("Esti minor si nu poti vota inca")

# 13. Scrie un program care primeste un pret de la tastatura si afiseaza
# un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
pret = float(input('pretul este'))
if pret<100:
    print('pretul este mai mic de 100')
else:
    print('pretul este mai mare')

# 14. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
# daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
nr1 = int(input('nr 1'))
nr2 = int(input('nr 2'))
produs = nr1*nr2
if produs <= 1000:
    print(nr1*nr2)
else:
    print(nr1+nr2)

# 15. Se dau doua liste:
# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [1, 2, 3, 4, 5]
# Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
# In functie de rezultat, afiseaza un mesaj.
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
if lista_1[0]==lista_1[-1]:
    print('sunt egale')
else:
    print('nu sunt egale')

if lista_2[0]==lista_2[-1]:
    print('sunt egale')
else:
    print('nu sunt egale')

# 16. Scrie un program care afiseaza de cate ori apare litera 'e' in
# stringul str_1 = 'Emma is a sofware developer.'
str_1 = 'Emma is a sofware developer.'
str_2 =str_1.lower()
print(str_1.count('e'))
print(str_2.count('e'))


# 17. Scrie un program in care citesti de la tastatura doua nr intregi,
# numite base si exponent.
# Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
# Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
# ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
# hint: exploreaza functia abs() si vezi cum o poti folosi
nr_1 = int(input('baza numarului este '))
nr_2 = int(input('exponentul numarului este '))
rezultatul = nr_1**nr_2.__abs__()  #abs = valoarea absoluta
print(f'rezultatul este {rezultatul}')

# 18. Scrie un program in care se citeste de la tastatura un string.
# Daca string-ul are numar impar de caractere, afiseaza un string care
# contine primul caracter, caracterul din mijloc al string-ului
# citit de la tastatura si ultimul caracter.
# Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
# si ultimul caracter  al string-ului citit de la tastatura.
str18 = input('ceva')
lungime_string = len(str18)
jumatate_string = len(str18) %2
x = len(str18)//2
print(x)
print(jumatate_string)
if lungime_string % 2==0:
    print(str18[0] + str18[-1])
else:
    print(str18[0] + str18[x] + str18[-1])

# 19. Se dau doua variabile:
str1 = 'Abc'
str2 = 'Xyz'
# Creeaza o variabila string, str3 formata din:
# - primul caracter din str1 cu litera mica
# - primul caracter din str2 cu litera mare
# - al doilea caracter din str1 cu litera mare
# - al doilea caracter din str2 cu litera mare
# - al treilea caracter din str1 cu litera mare
# - al treilea caracter din str2 cu litera mica
str3 = str1.lower()[0] + str2.upper()[0] + str1.upper()[1] + str2.upper()[1] + str1.upper()[2] + str2.lower()[2]
print(str3)
# ???20. Se da string-ul my_str = 'Emma is a data scientist who knows Python. Emma works at google.'
# Afiseaza ultima pozitie a substring-ului "Emma" in string-ul dat.
# HINT: vezi metoda ajutatoare string rstrip()
my_str = 'Emma is a data scientist who knows Python. Emma works at google.'
print(my_str.rstrip('Emma'))
