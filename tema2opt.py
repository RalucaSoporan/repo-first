
# C. OPTIONAL (nivel > MEDIU) (s-ar putea sa ai nevoie de Google)

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.


# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).

x = int(input('Introdu X: '))
if x < 0 and len(str(x)) > 4:
    print('X are minim 4 cifre')
if x > 0 and len(str(x)) >= 4:
    print('X are minim 4 cifre')
else:
    print('X are sub 4 cifre')





# 2. Verifica daca x are exact 6 cifre.
if x > 0 and len(str(x)) == 6:
    print('X are exact 6 cifre')
if x < 0 and len(str(x)) == 7:
    print('X are exact 6 cifre')
else:
    print('X nu are 6 cifre')

# 3. Verifica daca x este numar par sau impar.
if x % 2 ==0:
    print('nr par')
else:
    print('nr impar')

# 4. Avand trei variabile x, y, z (toate int) (le poti declara in cod sau citi de la tastatura),
# afiseaza in consola care este cel mai mare dintre ele.
x = 3
y = 5
z = 7
if x>y and x>z:
    print('x')
elif y>x and y>z:
    print('y')
else:
    print('z')

#5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid
#sau nu. (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau
#daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi).
x = 50
y = 40
z = 90
a = 20
b = 40
c = 70
suma_unghiuri = x+y+z
if x > 0 and y > 0 and z > 0 and a > 0 and b > 0 and c > 0:
    if suma_unghiuri == 180 or a + b > c:
        print('Este un triunghi valid')
    elif suma_unghiuri == 180 or a + c  > b:
        print('Este un triunghi valid')
    elif suma_unghiuri == 180 or b + c  > a:
        print('Este un triunghi valid')
    else:
        print('Nu este un triunghi valid')
else:
    print('Nu avem deloc triunghi')

# 6.
# a. Avand stringul: 'Coral is either the stupidest animal or the smartest rock', citește de la tastatura
# un număr x de tip int.
str = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('x = '))
# b. Afișează stringul fără ultimele x caractere.
# Exemplu: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'

if x<0:
    print(str[:-x])
else:
    print(str[:x])

# 7. Folosindu-te de același string de la
# exercițiul 6, declara un string nou care sa fie format din
# primele 5 caractere + ultimele 5 caractere

str_2 = print(str[0:5] + str[-5:])

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start
# al cuvântului rock - adică poziția in string la care începe cuvântul rock.
# (hint: este o funcție care te ajuta sa faci asta).

str_3 = print(str.find('rock'))
print(len(str))

# Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant.
# Output asteptat: 'Coral is either the stupidest animal or the smartest '

print(str[:-4])

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
# Se va folosi un assert.
# Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul
# si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)

prop = input('Introdu un string : ')
prop = prop.lower()
assert prop[0] == prop[-1]
print('caractere la fel')


# 10. Avand stringul '0123456789', afiseaza doar numerele pare si apoi doar numerele impare.
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

string = '0123456789'
print(f'Numerele pare {string[0:len(string):2]}')
print(f'Numerele impare {string[1:len(string):2]}')


# D. EXERCITII BONUS

# 1. Vrem sa cream o aplicatie pentru achizitionare de bilete de avion care sa primeasca drept inputuri
# urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport.
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti.
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la
# celalat parinte.
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi
# ca ar trebui testate.
# Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results
# sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

varsta = int(input('Introdu varsta: '))
cu_mama = int(input('Este insotit de mama: '))
cu_tata = int(input('Este insotit de tata: '))
pasaport = int(input('Are pasaport: '))
act_mama = int(input('Are act de la mama: '))
act_tata = int(input('Are act de la tata: '))
if varsta >= 18 and pasaport == 1:
    print('Ma pot imbarca')
elif (varsta < 18 and pasaport == 1 and cu_mama == 1 and cu_tata == 1):
    print('Ma pot imbarca')
elif varsta < 18 and pasaport == 1 and cu_mama == 1 and act_tata == 1:
    print('Ma pot imbarca')
elif varsta < 18 and pasaport == 1 and cu_tata == 1 and act_mama == 1:
    print('Ma pot imbarca')
else:
    print('Nu ma pot imbarca')
# Am folosit int la toate variabilele deoarece am asimilat pe True ca fiind 1,
# iar False orice alta cifra, in principiu 0


# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random.
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online.
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator.
# - Verifica si afiseaza daca utilizatorul a ghicit numarul.
# - Vor exista 3 optiuni care vor trebui tratate:
# a. Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# b. Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# c. Ai ghicit. Felicitari! Ai ales x si zarul a fost y.

import random
dice_roll = random.randint(0,9)
print(dice_roll)
numar_ales = int(input('Alege numar: '))
if numar_ales < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ales} dar a fost {dice_roll}.')
elif numar_ales > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ales} dar a fost {dice_roll}.')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {numar_ales} si zarul a fost {dice_roll}.')

# 3. Verifica daca varsta introdusa de utilizator este mai mare
# decat 18 ani.

varsta= int(input('varsta='))

if varsta > 18:
    print('este mai mare')
else:
    print('nu este mai mare')



# 4. Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
pret = int(input('pretul produsului este:'))
if pret <= 100:
    print('pretul e mai mic')
else:
    print('pretul e mai mare')

# 5.
# a. Citeste un numar de la tastatura.
# b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
nr = int(input('Tasteaza un numar:'))
if nr % 2 == 0:
    print('numarul e par')
else:
    print('numar impar')

# 6.
# a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
# b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
# c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".

viteza_medie = int(input('Scrie viteza:'))
if viteza_medie <= 50:
    print('Viteza normala')
elif viteza_medie > 50:
    print('Viteaza depasita')

# 7. Citeste de la tastatura varsta utilizatorului si afiseaza categoria
# de varsta in care se incadreaza.
# Tine cont de aceste categorii de varsta:
# intre 0-18 ani: minor
# intre 18-65 ani: adult
# peste 65 ani: senior

varsta = int(input('Introdu varsta ta: '))
if varsta >=0 and varsta < 18 :
    print('Esti minor')
elif varsta >= 18 and varsta <= 65:
    print('Esti adult')
elif varsta > 65:
    print('Senior')
else:
    print('Nu te incadrezi in nici o categorie')


# 8. Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
# cosul de cumparaturi, in functie de totalul cosului de cumparaturi
# Reducerea se aplica in felul urmator:
# - Total este intre 100 si 200 lei -> reducere 10%
# - Total intre 200 - 300 lei -> reducere 15%
# - Total intre 300-400 -> reducere 20 %
# - Total mai mare de 400 -> reducere 30 %.
# a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
# b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
# dupa aplicarea reducerii.

cos= float(input('valoare cos'))

if 100 <= cos < 200:
    print(cos - (cos * 10 / 100))
elif 200<= cos < 300:
    print(cos -(cos * 20 /100 ))
elif cos <=400:
    print(cos - (cos * 30 / 100))
else:
    print('nu are reducere')