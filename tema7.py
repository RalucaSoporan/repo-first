"""
1.Git setup

OBLIGATORIU!
Creati-va cont de github si incarcati intr-un repo nou tot ce am facut pana acum la ore
Curs git/github
https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
"""

"""
!! 2. Faceti urmatoarele exercitii dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
"""
"""
1. ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod
import math
class FormaGeometrica(ABC):
    math.pi= 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')


"""
2. INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
"""
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        print(f'Aria patratului este {self.__latura*self.__latura}')

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter : Latura are lungimea de {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        print(f'Setter: latura este {latura_noua}')
        self.__latura = latura_noua

    @latura.deleter
    def latura(self):
        print(f' Deleter: Am sters lungimea laturii')
        self.__latura = None

patrat1 = Patrat(5)
print(patrat1.latura)
(patrat1.aria())
(patrat1.descrie())
patrat1.latura = 9
patrat1.descrie()
patrat1.aria()
del patrat1.latura
print(patrat1.latura)




"""
3. Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
"""
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__r = raza

    def aria(self):
        print(f'Aria cercului este {self.__r*self.__r*math.pi}')

    @property
    def raza(self):
        return self.__r

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__r}')
        return self.__r

    @raza.setter
    def raza(self, raza_noua):
        print(f'Setter: noua raza este {raza_noua}')
        self.__r= raza_noua

    @raza.deleter
    def raza(self):
        print(f'Deleter: am sters raza')
        self.__r=None

cerc1 = Cerc(5)
print(cerc1.raza)
(cerc1.aria())
(cerc1.descrie())
cerc1.raza = 9
cerc1.descrie()
cerc1.aria()
del cerc1.raza
print(cerc1.raza)



"""
4. POLYMORPHISM 
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’

Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
"""


"""
5. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public

Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4
"""
