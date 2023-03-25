# TEMA 2: Metoda input(), metode string, operatori, conditionale

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link catre video: https://www.itfactory.ro/8174437-intro-in-programare

# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. Citeste de la tastatura numele, citeste apoi de la tastatura prenumele. Afiseaza cate caractere are numele complet
# (nume + prenume), afisand propozitia 'Numele complet are x caractere.', unde x este numarul total de caractere.
nume = input("numele")
prenume = input('prenume')
x = len(nume + prenume)
print(f'Numele complet are {x} caractere')



# 2. Citeste de la tastatura lungimea, citeste apoi de la tastatura latimea. Afiseaza aria dreptunghiului cu lungimea si
# latimea citite de la tastatura, afisand propozitia 'Aria dreptunghiului este x.', unde x este valoarea ariei.

lungimea =float(input('lungimea este'))
latimea = float(input('latimea este'))
x =( lungimea * latimea)
print(f'Aria dreptunghiului este {x}')

# 3. Avand stringul: 'Coral is either the stupidest animal or the smartest rock.', afisati de cate ori apare cuvantul
# 'the' in acesta.

my_str = 'Coral is either the stupidest animal or the smartest rock.'

print(my_str.count('  the '))

# 4. Folosing acelasi string de la punctul 2, inlocuieste cuvantul 'the' cu 'THE' peste tot in propozitie si printeaza
# rezultatul
print(my_str.replace(' the ', ' THE '))

# 5. Folosind acelasi string de la punctul 2, folositi un assert ca sa verificati daca acest string contine doar
# numere.
#assert my_str.isnumeric()== True
print("adevarat")
# 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:
a = 'Ana are mere Rosii'

# # a. endswith()
print(a.endswith('i')) # il intrebam cu ce se termina
print(a.endswith('m'))

# b. index()
print(a[0:3])
print(a[:7])
print(a[7:])
print(a.index('are')) #pozitia la care incepe
print(a.index('Ana'))
print(a.index('m'))

# c. lower() # toate literele mici
print(a.lower())
print(a.lower())
# d. replace() # rescrie
print(a.replace('a', 'x'))
print(a.replace('e', 'y'))
# e. strip() # elimina sau truncheaza elemente date de la inceputul sau sf sirului
print(a.strip('A'))
print(a.strip('Ana'))
# f. split() #
b = 'baiatul-are-5-ani'
print(b.split('-'))


# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.
x = int(input('Variabila x este'))


# 6. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.
#if else functioeaza ca o intersectie, daca nu o iau in stanga, atunci o iau in dreapta

# 7. Verifica si afiseaza daca x este numar natural sau nu.
# (un numar se considera natural daca este numar intreg mai mare ca 0)
if x >=0:  #???

    print('numar natural')
else:
    print('nu')

# 8. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru (adica 0).
if x>0:
    print('numar pozitiv')
elif x<0:
    print('numar negativ')
else:
    print('egal cu 0')

# 9. Verifica si afiseaza daca x este intre -2 si 13 (incluzand capetele de interval).
if -2 <= x <=13:
    print('numar cuprins in interval')
else:
    print('numar in afara intervalului')

# 10.
# a. Declara o noua variabila numita y, de tip int.
y = int(input('variabila y este'))

# b. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
if x-y<5:
    print('adevarat')
else:
    print('fals')

# 11. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
if not(5 <= x <= 27):
    print('nu este inclus')
else:
    print("este inclus")

# 12.
# a. Declara o noua variabila numita y, de tip int.
y = 8
# b. Verifica si afiseaza daca x si y sunt egale. Daca nu, afiseaza care din ele este mai mare.
if x == y:
    print('sunt egale')
elif x < y:
    print ('x >')
else:
    print(' y >')

# 13. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
x = int(input('x='))
y = int(input('y='))
z = int(input('z ='))

if x==y==z:
    print('triunghi echilateral')
elif x==y or x==z or y==z:
    print('triunghi isoscel')
else:
    print('triunghi oarecare')


# 14. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.


litera= input('Introdu caracter: ')
if litera.lower() in ('a', 'e', 'i', 'o', 'u'):
    print('Vocala ')
elif litera.upper() in ('A', 'E', 'I', 'O', 'U'):
    print('Avem o vocala ')
else:
    print('Avem o consoana')

# 15. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = float(input('nota este'))
if nota>9:
    print('A')
elif nota>8:
    print('B')
elif nota>=7:
    print('C')
elif nota>6:
    print('D')
elif nota>4:
    print('E')
else:
    print('F')


