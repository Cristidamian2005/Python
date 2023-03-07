# # 1.Clasa Cerc
# # Atribute: raza, culoare
# # Constructor pentru ambele atribute
# # Metode:
# # ● descrie_cerc() - va PRINTA culoarea și raza
# # ● aria() - va RETURNA aria
# # ● diametru()
# # ● circumferinta()
#
# import math
#
#
# class Cerc:
#     raza = 5
#     culoare = 'alb'
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f'Cerc cu raza {self.raza} de culoare {self.culoare}')
#
#     def aria(self):
#         return math.pi * self.raza * self.raza
#
#     def diametru(self):
#         return 2 * self.raza
#
#     def circumferinta(self):
#         return 2 * math.pi * self.raza
#
#
# cerc1 = Cerc(10, "verde")
# cerc2 = Cerc(15.7, 'roz')
#
# cerc1.descrie_cerc()
# cerc2.descrie_cerc()
#
# print(f'Aria cerc1 este {cerc1.aria()}')
# print(f'Aria cerc2 este {cerc2.aria()}')
#
# print(f'Diametrul cerc1 este {cerc1.diametru()}')
# print(f'Diametrul cerc2 este {cerc2.diametru()}')
#
# print(f'Circumferinta cerc1 este {cerc1.circumferinta()}')
# print(f'Circumferinta cerc2 este {cerc2.circumferinta()}')


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

# class Dreptunghi:
#     lungime = 0
#     latime = 0
#     culoare = None
#
#     def descrie(self):
#         print(f'Dreptunghiul are lungimea de {self.lungime} , latimea de {self.latime} si culoarea {self.culoare}')
#
#     def aria(self):
#         print(f'Dreptunghiul are aria de {self.lungime * self.latime}')
#
#     def perimetru(self):
#         print(f'Dreptunghiul are perimetrul de {2 * (self.lungime + self.latime)}')
#
#     def schimba_culoarea(self, culoare):
#         self.culoare = culoare
#         print (f'Noua culoare este {self.culoare}')
#
#
# drept_1 = Dreptunghi()    # am inteles eu bine ca daca nu ai constructor explicit atunci constructorul implicit iti
# drept_1.lungime = 5         # creeaza obiectele cu valorile definite implicit? si doar prin metode clasei poti schimba valorile?
# drept_1.latime = 3
# drept_1.culoare = 'verde'
#
# drept_1.descrie()
# drept_1.aria()
# drept_1.perimetru()
# drept_1.schimba_culoarea('roz')
# drept_1.descrie()


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

# class Angajat:
#     nume = None
#     prenume = None
#     salariu = 0
#
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Salariatul {self.nume} {self.prenume} care are salariul de {self.salariu} lei')
#
#     def nume_c(self):
#         print(f'Numele complet al angajatului este: {self.nume} {self.prenume}')
#
#     def salariu_lunar(self):
#         print(f'Salariul lunar este de {self.salariu} lei')
#
#     def salariu_anual(self):
#         print(f'Salariul anual este de {self.salariu * 12} lei')
#
#     def marire_salariu(self, procent):
#         self.salariu += self.salariu * procent/100
#         print(f"Salariul dupa marire este {self.salariu}")
#
#
# a_1 = Angajat("Petrescu", "Gigel", 2000)
# a_1.descrie()
# a_1.nume_c()
# a_1.salariu_lunar()
# a_1.salariu_anual()
# a_1.marire_salariu(10)


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

# class Cont:
#     iban = 0
#     sold = 0
#     titular = None
#
#     def __init__(self, iban, sold, titular):
#         self.iban = iban
#         self.sold = sold
#         self.titular = titular
#
#     def afisare(self):
#         print(f"Titularul {self.titular} are in contul {self.iban} suma de {self.sold} lei")
#
#     def debitare(self, suma):
#         if self.sold >= suma:
#             self.sold -= suma
#             print(f"Ati extras suma de {suma} lei din cont. Mai aveti {self.sold} lei")
#         else:
#             print('Fonduri insuficiente')
#
#     def creditare(self, suma):
#         self.sold += suma
#         print(f'Ati depus {suma} lei. Acum aveti {self.sold} lei in cont')
#
#
# cont_1 = Cont(1234567890, 150, "Vasile Gheorghe")
# cont_1.afisare()
# cont_1.debitare(30)
# cont_1.debitare(150)
# cont_1.creditare(50)


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

# from datetime import date
#
#
# class Factura:
#
#     seria = 12345
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self. cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate =cantitate
#
#     def schimba_pretul(self, pret_bucata):
#         self.pret_buc = pret_bucata
#
#     def schimba_nume_produs(self, nume_produs):
#         self.nume_produs = nume_produs
#
#     def genereaza_factura(self):
#         cost_total = self.cantitate * self.pret_buc
#         data_azi = date.today().strftime('%d/%m/%Y')
#         print(f'Factura seria {Factura.seria} numar {self.numar}\nData: {data_azi}')
#         print('Produs | Cantitate | Pret bucata | Total')
#         print(f'{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {cost_total}')
#
#
# factura1 = Factura(1, "Volvo", 1, 12000)
# factura1.schimba_cantitatea(2)
# factura1.schimba_pretul(13800)
# factura1.schimba_nume_produs('Mercedes')
# factura1.genereaza_factura()
#
# factura2 = Factura(2, "cai ", 5, 4000)
# factura1.schimba_cantitatea(6)
# factura1.schimba_pretul(4800)
# factura1.schimba_nume_produs('cai frumosi')
# factura1.genereaza_factura()


# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0


# class Masina:
#     marca = 'Dacia'
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = {'alb', 'verde', 'portocaliu', 'orange', 'negru', 'violet'}
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(f'Maina marca {self.marca} , model {self.model}, culoare {self.culoare}, inmatriculata {self.inmatriculata}')
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#
#     def vopsire(self, culoare):
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#             print(f'Am vopsit masina in culoarea {self.culoare}')
#         else:
#             print(f'Culaorea {culoare} nu este disponibila')
#
#     def accelereaza(self, viteza_actuala):
#         if viteza_actuala < 0:
#             print('Eroare! Nu poti accelera negativ')
#         elif viteza_actuala < self.viteza_maxima:
#             self.viteza_actuala = viteza_actuala
#             print(f'Ai accelerat pana la viteza de {self.viteza_actuala}')
#         else:
#             self.viteza_actuala = self.viteza_maxima
#             print(f'Ai accelerat pana la viteza maxima de {self.viteza_actuala}')
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#         print('Ai oprit masina')
#
#
# sandero = Masina("Sandero", 180)
# sandero.descrie()
# sandero.inmatriculare()
# sandero.descrie()
# sandero.vopsire('fucsia')
# sandero.vopsire('portocaliu')
# sandero.descrie()
# sandero.accelereaza(100)
# sandero.accelereaza(90)
# sandero.accelereaza(-10)
# sandero.accelereaza(220)
# sandero.franeaza()


# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict

# class TodoList:
#     todo = {}
#
#     def adauga_task(self, nume, descriere):
#         self.todo[nume] = descriere
#
#     def finalizeaza_task(self, nume):
#         if nume in self.todo:
#             del self.todo[nume]
#             print(f'Am sters taskul {nume}')
#         else:
#             print('Taskul nu e in ToDo-list')
#
#     def afiseaza_to_do_list(self):
#         print('Taskurile sunt: ')
#         for nume in self.todo:
#             print(nume)
#
#     def detalii_suplimentare(self, nume):
#         if nume in self.todo:
#             print(f'Detaliile task-ului "{nume}" sunt: {self.todo[nume]}')
#         else:
#             da_nu = input(f'Task-ul "{nume}" nu e in lista . Adaugam? (da/nu): ')
#             if da_nu =='da':
#                 detalii = input('Descrieti taskul: ')
#                 self.adauga_task(nume, detalii)
#                 print(f'Am adaugat taskul {nume}.')
#             else:
#                 print('Bye!')
#
#
# lista1 = TodoList()
# lista1.adauga_task('revizie', 'schimbat filtre, ulei, distributie, pompa apa')
# lista1.afiseaza_to_do_list()
# lista1.detalii_suplimentare('revizie')
# lista1.detalii_suplimentare('pizza')
# lista1.afiseaza_to_do_list()
# lista1.detalii_suplimentare('pizza')


