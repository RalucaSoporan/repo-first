# TEMA 1

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza inregistrarea sesiunii 1 si ia notite
# 2. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE" (daca nu ai facut-o deja), sectiunea "Variable si Tipuri de date"
# 3. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE", sectiunea "Operatori si Flow Control".
# LINK curs "PRIMII PASI IN PROGRAMARE": https://www.itfactory.ro/8174437-intro-in-programare/


# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila.
# Variabilele sunt simple sectiune de memorie rezervate stocarii anumitor informatii

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool.
# Valorile le alegeti voi dupa preferinte.
#string
nume = 'Raluca'
print(nume)
#int
varsta = 34
print(varsta)
#float
greutate = 80.5
print(greutate)
#bool
casatorita = True
print(casatorita)
# 3. Utilizati functia type(), pentru a verifica daca variabilele declarate la punctul 2 au tipul de date asteptat.
print(type(nume))
print(type(varsta))
print(type(greutate))
print(type(casatorita))
# 4. Rotunjiti variabila definita ca tip float, folosindu-va de functia round() si salvati aceasta modificare in aceeasi
# variabila (suprascriere). Verificati apoi tipul acesteia.
print(round(greutate))
print(type(round(greutate)))
greutate = round(greutate)
print(greutate)
# 5. Folositi functia print() pentru a printa in consola 4 propozitii, folosind cele 4 variabile.
# (Rezolvati nepotrivirile de tip prin ce modalitate doriti)
print(f'Ma numesc {nume} si am varsta de {varsta}')
print(f'Ma numesc {nume } si cantaresc {greutate}')
print(f'Ma numesc {nume} si sunt casatorita {casatorita}')
print('Ma numesc ' + nume + ' si am varsta de ' + str(varsta))

# 6.
# a. Defineste o variabila float cu valoarea 1.5 .
m = 1.5
# b. Verifica daca variabila este egala cu 1.5 .
assert m == 1.5
print('valoare adevarata')
# c. Verifica daca variabila este egala cu true. Ce observi?
#assert m == True
#print("adevarat") #apare eroare

# d. Cum poti face ca assert-ul de la punctul c sa treaca?
assert bool(m)
print('Am modificat valoarea')
#am modificat in int in boolean

