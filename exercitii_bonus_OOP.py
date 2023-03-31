"""
EXERCITII BONUS - OOP

Aceste exercitii sunt OPTIONALE!

"""

"""
1. 
a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).

b. Implementeaza proprietatea password care va incapsula atributul privat
password.
Va avea:
- getter:
In getter verificam daca parola a fost setata (daca are valoare).
Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
cu lungimea parolei.
Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.
- setter:
In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
urmatoarele conditii:
    -- are minim 10 caractere
    -- are cel putin o litera mare
Daca aceste conditii se indeplinesc atunci setam parola.
Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.

c. Metode:
- Metoda login: verificam ca user-ul are atat username, email si parola.
Daca are, atunci afisam mesajul "Conectat".
Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"

d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
Afiseaza toate atributele/metodele/proprietatile.
"""
class User:
    def __init__(self, username, mail):
        self.username = username
        self.mail = mail
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.getter
    def password(self):
        if self.__password != None:
            print('*'*len(self.__password))
        else:
            print('Parola nu a fost setata')

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 10:
            for i in new_password:
                if str(i).upper()== i:
                    self.__password= new_password
                    print('Parola setata')
            else:
                print('Parola trebuie sa contina si litere mari')
        else:
            print('Parola ta nu are suficiente caractere')

    def login(self):
        if self.username and self.mail and self.__password != None:
            print('Conectat')
        else:
            print('Nu te-ai conectat')


user1 = User('papalapte', 'papalapte@yahoo')
user1.password = 'maria'
user1.password = 'alabalaportocala'
user1.password = 'Alabalaportocala'
(user1.password)
user1.login()

user2 = User('alabala', 'alabala@yahoo')
user2.password= 'Alabalaportocala'
(user2.password)
user2.login()

print('ex 2')
"""
2.
a. Defineste clasa abstracta Person.
Metode abstracte: wake_up, sleep, eat.
Metoda: describe -> afiseaza mesajul "O persoana se trezeste, mananca si doarme."

b. Defineste clasa Student.
Clasa Student implementeaza clasa abstracta Person.
Atribute in constructor: name, university, grade.
Metode describe -> afiseaza SI mesajul:
Studentul x, studiaza la universitatea y si are nota generala z.

c. Defineste clasa Employee.
Clasa Employee implementeaza cls abstracta Person.
Atribute in constructor: name, experience, salary.
Salary este un atribut privat!
Metoda describe -> afiseaza SI mesajul:
Angajatul x lucreaza de y ani.

d. Creeaza proprietatea salary care sa incapsuleze atributul privat salary.


"""
from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def wake_up(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
    @abstractmethod
    def eat(self):
        pass

    def describe(self):
        print("O persoana se trezeste, mananca si doarme.")




class Student(Person):
    def __init__(self, name, university, grade):
        self.name = name
        self.university = university
        self.grade = grade

    def describe(self):
        super().describe()
        print(f'Studentul {self.name}, studiaza la universitatea {self.university} si are nota generala {self.grade}.')
    def wake_up(self):
        print('Ma trezesc la ora 7')
    def sleep(self):
        print('Dorm minim 6 ore pe noapte')
    def eat(self):
        print('Mesele mele sunt variate')

class Employee(Person):
    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.__salary = salary

    def describe(self):
        super().describe()
        print(f'Angajatul {self.name} lucreaza de {self.experience} ani')

    @property
    def salary(self):
        return self.__salary

    def wake_up(self):
        print('Ma trezesc la ora 7')
    def sleep(self):
        print('Dorm minim 6 ore pe noapte')
    def eat(self):
        print('Mesele mele sunt variate')



# d. Creeaza proprietatea
# salary care sa incapsuleze atributul privat salary.

stundent1 = Student('Maria','UTCN', 9)
print(stundent1.name)
print(stundent1.university)
print(stundent1.grade)
stundent1.sleep()
stundent1.eat()
stundent1.wake_up()
stundent1.describe()

employee1 = Employee('Vasile', 6, 2500)
employee1.eat()
employee1.sleep()
employee1.wake_up()
employee1.describe()
print(employee1.salary)




