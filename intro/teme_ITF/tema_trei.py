# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a. Afiseaz-o
# b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
# varianta actuala (inversata)
# c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
# inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
# asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
# varianta inițială
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
# suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
# suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
# găsesc utilitatea în funcție de ce ne dorim in acel moment.

# note_m = []
# print(f"Lista goala este: {note_m}")
# print(type(note_m))
# note_m1 = list()
# print(type(note_m1))
# print(f"Lista 1 goala este: {note_m1}")
# print(f"Dimensiunea listei goale este: {len(note_m)}")
# print(f"Dimensiunea listei 1 goale este: {len(note_m1)}")


# note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
#
# #a
# print(f'Lista de note muzicale este: {note_muzicale}')

# # b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
# note_muzicale = note_muzicale[::-1]
# print(f'Lista de note muziacale in ordine inversa este {note_muzicale}')
#
# # c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
# # inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
# # asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
# # varianta inițială
# note_muzicale.reverse()
# print(f"Tare sucit mai esti :)) ! Schimbarea schimbarii este: {note_muzicale}")

#
# # 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
# print(f'Nota "do" apare de {note_muzicale.count("do")} ori')

# # 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
# list_1 = [3, 1, 0, 2]
# list_2 = [6, 5, 4]
# new_list = list_1 + list_2
# print(f'Prima varianta {new_list}')
# new_list_1 = list_1.extend(list_2)
# print(f'A doua varianta de ce afiseaza None ???  {new_list_1}')
# print(f'A doua varianta reloaded {list_1}')


# 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
# folosind o functie si apoi afiseaza din nou lista
# new_list.sort()
# print(f'Lista sortata {new_list}')
# new_list.pop(0)
# print(f'Lista sortata fara 0 :  {new_list}')


# 5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
# urmatoarele:
# - Lista este goala (IF)
# - Lista nu este goala (ELSE)

# Traiasca Google! :))
# Varianta 1
# if not new_list:
#    print('Empty list')
# else:
#    print('List is not Empty \n',new_list)
#
# # Varianta 2
#
# empty_list = []
# if len(empty_list) == 0:
#     print('Empty list')
# else:
#     print('Not Empty list')
#
# # Varianta 3
#
# # Checking whether the list object is equal to [](null list)
# if new_list == []:
#    print('Empty list')
# else:
#    print('List is not empty\n',new_list)

# 6. Foloseste o functie care sa goleasca lista de la exercitiul 3

# print(f'Lista golita este: {new_list.clear()}')


# 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
# afiseze ca lista e goala

# if not new_list:
#    print('Empty list')
# else:
#    print('List is not Empty \n',new_list)


# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
# afisezi Elevii (cheile)

# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f'Numele elevilor: {dict1.keys()}')

# 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie

# print(f'Ana a luat nota {dict1.get("Ana")}')
# print(f'Gigel a luat nota {dict1.get("Gigel")}')
#print(f'Dorel a luat nota {dict1.get("Dorel")}')

# 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# - Modifica nota lui Dorel in 6
# - Printeaza nota lui dupa modificare

# dict1["Dorel"] = 6
# print(f'Dorel a luat nota {dict1.get("Dorel")}')

# 11. Imagineaza-ti ca Gigel se transfera din clasa.
# - Cauta o functie care sa il stearga
# Vine un coleg nou.
# - Adaugati-l in lista pe Ionica, cu nota 9
# - Printati dictionarul cu noii elevi

# dict1.pop("Gigel")
# print(dict1)
# dict1["Ionica"] = 9
# print(dict1)

# 12. Ai urmatoarele seturi:

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
#
# # - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# # - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
#
# zile_sapt.add('luni')
# print(zile_sapt)

# 13. Foloseste un if si verifica daca:
# - Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
# regasesc intre elementele din setul zile_sapt)
# - Weekend nu este un subset al zilelor din sapt
# Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
# punct de mai sus va fi un boolean
#
# if weekend.issubset(zile_sapt):
#     print('Weekend  este un subset al zilelor din sapt')
# else:
#     print('Weekend  NU este un subset al zilelor din sapt')
#
# if weekend <= zile_sapt:
#     print('Weekend  este un subset al zilelor din sapt')
# else:
#     print('Weekend  NU este un subset al zilelor din sapt')


# 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# sunt in weekend si invers)

# print(zile_sapt - weekend)
# print(weekend - zile_sapt)
# print(zile_sapt.difference(weekend))
# print(weekend.difference(zile_sapt))

# 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
# ambele seturi). Hint: Va puteti folosi de o functie.

# print(zile_sapt.intersection(weekend))


# zzzzzzzzzzzzzzzzzzzzzzzzzz   Exerciții Opționale  zzzzzzzzzzzzzzzzzzzzz

# 1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
# - Declara o lista cu 5 jucatori: lista_jucatori_teren
# - Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
# - Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
# - Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
# - SCHIMBARI_MAX va fi o constanta cu valoarea 3

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
# - Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
# teren
# - Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
# - Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
# de rezerva
# - Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
# variabilelor voastre)
# Daca jucatorul pe care vrem sa il schimbam nu e in teren:
# - Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Altfel, afisati ecran: ‘mai aveti z schimbari’



################ NU E CORECT #############################
# lista_jucatori_teren = [ 'hagi', 'popescu', 'mutu', 'petrescu', 'chivu']
# lista_jucatori_rezerva = [ 'hagi1', 'popescu1', 'mutu1', 'petrescu1', 'chivu1']
# print(f'Prezentam echipele {lista_jucatori_teren}')
# print(f'Prezentam rezervele {lista_jucatori_rezerva}')
# lista_jucatori_scosi = []
# schimbari_max = 3
# schimbari_efectuate = 0


# jucator_iesit = input(f' Introdu jucatorul care vrei sa iasa: ')
# if jucator_iesit not in lista_jucatori_teren:
#     print('Jucatorul nu se afla pe teren sau ati introdus un nume gresit')
#     jucator_iesit = input(f' Introdu jucatorul care vrei sa iasa: ')
# jucator_intrat = input(f' Introdu jucatorul care vrei sa intre: ')
# if jucator_intrat not in lista_jucatori_rezerva:
#     jucator_intrat = input('Jucatorul nu se afla printre rezerve. Reintroduceti numele: ')
# elif jucator_intrat in  lista_jucatori_teren:
#      jucator_intrat = input('Jucatorul este deja pe teren. Alegeti alt jucator: ')
# if schimbari_efectuate > schimbari_max:
#     print(' Nu mai ai schimbari! ')
# elif (jucator_intrat in lista_jucatori_rezerva) and (jucator_iesit in lista_jucatori_teren) and (jucator_intrat not in lista_jucatori_teren) and (jucator_iesit not in lista_jucatori_rezerva):
#     lista_jucatori_teren.remove(jucator_iesit)
#     lista_jucatori_teren.append(jucator_intrat)
#     lista_jucatori_scosi.append(jucator_iesit)
#     lista_jucatori_rezerva.remove(jucator_intrat)
#     schimbari_efectuate += 1
#     print(f'a intrat {jucator_intrat}, a iesit {jucator_iesit}. Mai aveti {schimbari_max-schimbari_efectuate} schimbari ')
#     print(f' Jucatori teren: {lista_jucatori_teren}')
#     print(f' Jucatori rezerva: {lista_jucatori_rezerva}')
#     print(f' Jucatori schimbati: {lista_jucatori_scosi}')
#
# elif jucator_iesit not in lista_jucatori_teren:
#     print(f'nu se poate efectua schimbarea deoarece {jucator_iesit} nu e pe teren')
# else:
#     print(f'mai aveti {schimbari_max-schimbari_efectuate} schimbari')


