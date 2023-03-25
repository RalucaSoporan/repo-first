# Exerciții RECOMANDATE - grad de dificultate: Ușor

# 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link video: https://www.itfactory.ro/8174437-intro-in-programare/

# EXERCITII OBLIGATORII

# 1.
# a. Declara o lista, note_muzicale, in care sa pui do re mi etc pana la do.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# b. Afiseaz-o.

print(note_muzicale)

# c. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata).

print(note_muzicale[::-1])

# d. Aplica o metoda pe lista care banuiesti ca face același lucru, adica sa ii inverseze ordinea.
# (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat)
# si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială.
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
# sau sa o salvezi intr-o listă nouă.
# Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări.
# Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.

note_muzicale.reverse()
print(note_muzicale)

# e. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

print(note_muzicale.count('do'))

# 2. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante prin care sa le unesti intr-o singura lista.

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list3 = list1 + list2
print(list3)
list4 = list1.append(list2)
print(list4)

# 3.
# a. Sorteaza si afiseaza lista generata la exercitiul anterior.
list3.sort()
print(list3)

# b. Sterge numarul 0 din lista folosind o functie/metoda ajutatoare si apoi afiseaza din nou lista.
list3.remove(0)
print(list3)

# 4. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# Lista este goala (IF)
# Lista nu este goala (ELSE)

if not list3:
    print('lista este goala')
else:
    print('lista nu este goala')

# 5. Foloseste o functie care sa goleasca lista de la exercitiul 3/ sa o transforme in lista goala.
list3.clear()
print(list3)

# 6. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala.
if not list3:
    print('lista este goala')
else:
    print('lista nu este goala')


# 7. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5},
# foloseste o functie ca sa afisezi Elevii (cheile).
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorin': 5
}
print(dict1)
print(dict1.keys())
# 8. Printeaza cei 3 elevi din dictionarul de la exercitiul 7 si respectiv notele lor.
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota ' + str(dict1['Ana']))
print( f'Gigel a luat nota ' + str(dict1['Gigel']))
print(f'Dorin a luat nota ' + str(dict1['Dorin']))


# 9. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# Modifica nota lui Dorel in 6
dict1['Dorin'] = 6
print(dict1)

# Printeaza nota lui dupa modificare
print(dict1['Dorin'])

# 10. Imagineaza-ti ca Gigel se transfera din clasa.
# a. Cauta o functie care sa il stearga
dict1.pop('Gigel')
print(dict1.get(f'Gigel', 'nu mai face parte din elevi'))
print(dict1)

# b. Vine un coleg nou.
# Adaugati-l in lista pe Ionica, cu nota 9.

dict1['Ionica'] = 9

# c. Printati dictionarul cu noii elevi
print(dict1)

