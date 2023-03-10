# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")


# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):
    __latura = None

    # def __init__(self, latura):
    #     self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)

    def set_latura(self, latura):
        if latura <= 0:
            print("Eroare")
        else:
            self.__latura = latura

    def get_latura(self):
        return self.__latura

    def del_latura(self):
        del self.__latura

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)


class Cerc(FormaGeometrica):
    __raza = None

    def __init__(self, raza):
        self.__raza = raza

    def set_raza(self, raza):
        if raza <= 0:
            print("Eroare")
        else:
            self.__raza = raza

    def get_raza(self):
        return self.__raza

    def del_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.__raza * self.__raza

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui

    def descrie(self):
        print("Eu am colturi")


patraru = Patrat()
patraru.set_latura(-3)
patraru.set_latura(7)
patraru.descrie()
print(patraru.aria())
patraru.del_latura()
# patraru.aria()








