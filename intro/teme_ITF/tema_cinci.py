# # Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# #1.Funcție care să calculeze și să returneze suma a două numere
#
# def suma_a_b(a, b):
#     c = a + b
#     return c
#     # print(f' Suma celor doua numere este {c}')
#
#
# print(suma_a_b(11, 14))
# print(suma_a_b(-23.5, 16/3))


# # 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
#
# def par_impar(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(par_impar(23))
# print(par_impar(4))

#
# # 3. Funcție care returnează numărul total de caractere din numele tău complet.
# # (nume, prenume, nume_mijlociu)
#
# def total_caractere(nume):
#     contor = 0
#     for caracter in nume:
#         if str(caracter) != ' ':
#             contor = contor + 1
#     return contor
#
#
# print(total_caractere('Mihai Popescu'))
# print(total_caractere(' Damian '))
# print(total_caractere('Damian Cristinel'))


# # 4. Funcție care returnează aria dreptunghiului
#
# def aria_d(lu, la):
#     return lu * la
#
#
# print(aria_d(15, 30))
# print(aria_d(9.5, 3))
# print(aria_d(0.7, 3))


# # 5. Funcție care returnează aria cercului
#
# def aria_cerc():
#     pi = 3.14
#     r = float(input(f'Va rugam introduceti raza: '))
#     aria_cerc = pi * r * r
#     return aria_cerc
#
#
# print(f'Aria cercului este {aria_cerc()}')

#
# # 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# # și False dacă nu găsește.
#
# def x_string (x, string):
#     if x.lower() in string.lower():
#         return True
#     else:
#         return False
#
#
# print(x_string('x' , 'an tan te tini mane pe x'))
# print(x_string('Z' , 'an tan te tini z mane pe '))
# print(x_string('Z' , 'an tan te tini  mane pe '))


# # 7. Funcție fără return, primește un string și printează pe ecran:
# # ● Nr de caractere lower case este x
# # ● Nr de caractere upper case exte y
#
# def low_up(text):
#     low = 0
#     up = 0
#     for caracter in text:
#         if caracter.islower():
#             low += 1
#         elif caracter.isupper():
#             up += 1
#     print(f'Caractere low: {low}')
#     print(f'Caractere up: {up}')
#
#
# low_up('Ana Maria Moldovan')
# low_up('AAAa =-')
# low_up('AB-G ac.,.bl =-')


# # 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# # numerele pozitive
#
# def lista_numere(numere):
#     pozitive = []
#     for numar in numere:
#         if numar >= 0:
#             pozitive.append(numar)
#     return pozitive
#
#
# print(lista_numere([3, 6, -9, 6, -5, 0, 11, -13.5, 56.8] ))
# print(lista_numere([-3, 6, 9, -6, 5, 0, -11, 13.5, -56.8] ))


# # 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# # ● Primul număr x este mai mare decat al doilea nr y
# # ● Al doilea nr y este mai mare decat primul nr x
# # ● Numerele sunt egale.
#
# def doua_numere(x, y):
#     if x > y:
#         print(f'Numarul {x} este mai mare decat numarul {y}')
#     elif y > x:
#         print(f'Numarul {y} este mai mare decat numarul {x}')
#     else:
#         print(f'Numarul {y} este egal cu numarul {x}')
#
#
# doua_numere(15, 18)
# doua_numere(15, 15)
# doua_numere(17.7, 10)


# # 10. Funcție care primește un număr și un set de numere.
# # ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# # ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# # returnează False
#
# def numar_set(nr, set):
#     if nr not in set:
#         set.add(nr)
#         print(f'Am adaugat numarul {nr} in set')
#         return True
#     else:
#         print(f'Nu am adaugat numarul {nr} in set')
#         return False
#
#
# print(numar_set(0, {6, 5, 4, 3, 2}))
# print(numar_set(2, {6, 5, 4, 3, 2}))
# print(numar_set(-11, {6, 5, 4, 3, 2}))


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna

# def luna_an(luna):
#     zile_luna = {"Ianuarie": 31,
#                  "Februarie": 28,
#                  "Martie": 31,
#                  "Aprilie": 30,
#                  "Mai": 31,
#                  "Iunie": 30,
#                  "Iulie": 31,
#                  "August": 31,
#                  "Septembrie": 30,
#                  "Octombrie": 31,
#                  "Noiembrie": 30,
#                  "Decembrie": 31}
#     print(f' Luna {luna} are {zile_luna[luna]} zile')
#
#
# luna_an('Ianuarie')
# luna_an('Iunie')
# luna_an('Februarie')


# # 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# # împărțirea a două numere.
# # În final vei putea face:
# # a, b, c, d = calculator(10, 2)
# # ● print("Suma: ", a)
# # ● print("Diferenta: ", b)
# # ● print("Inmultirea: ", c)
# # ● print("Impartirea: ", d)
#
# def calculator(a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultire = a * b
#     impartire = a / b
#     return suma, diferenta, inmultire, impartire
#
#
# a, b, c, d = calculator(17, 5)
# print(f'Suma este {a}')
# print(f'Diferenta este {b}')
# print(f'Inmultirea este {c}')
# print(f'Impartirea este {d}')


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }


                    ###### !!!!!!!!de intrebat cum se face, e gresit !!!!!!!!! #######




# def lista_cifre(lista_cif):
#     cifre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     dictionar = {
#         0: 0,
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0,
#         7: 0,
#         8: 0,
#         9: 0
#     }
#     for cifra in lista_cif:
#         if cifra in dictionar:
#             cifre[cifra] += 1
#         else:
#             cifre[cifra] = 1
#
#     return dictionar
#
#
# print(lista_cifre([1,2,3,4,5,6,7]))

# # 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
#
# def maxim_numere(a, b, c):
#     return max(a, b, c)
#
# print(maxim_numere(1, 4, 7))
# print(maxim_numere(56, 0.3, -5 ))
# print(maxim_numere(-11, -0.3, 0 ))


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

# def suma_nr(a):
#     suma = 0
#     for i in range(0,a+1):
#         suma += i
#     return suma
#
#
# print(suma_nr(4))


# Exerciții Opționale - Bonus

# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
#
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}


# def liste(lista1, lista2):
#     lista_comuna = list()
#     for numar in lista1:
#         if numar in lista2 and numar not in lista_comuna:
#             lista_comuna.append(numar)
#     print(lista_comuna)
#
#
# lista1 = [1, 2, 9, 3, 7, 2, 5]
# lista2 = [11, 5, 3, 4, 7, 2 ]
# lista3 = [6, 9, 15, 35, 3, 7 ]
# liste(lista1, lista2)
# liste(lista1, lista3)
# liste(lista2, lista3)


# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

# def reducere_pret(pret, procent):
#     pret_redus = pret
#     if procent > 0 and procent < 100:
#         pret_redus -= procent * pret / 100
#     else:
#         print("Reducere invalida")
#
#     return pret_redus
#
#
# print(reducere_pret(100, 25))
# print(reducere_pret(80, 10))
# print(reducere_pret(80, -10))
# print(reducere_pret(80, 110))


# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

# import datetime
# import pytz
# from datetime import datetime
#
#
# def data_ora_ro():
#     romania = datetime.now()
#     print('Data/Ora Romania: ', romania.strftime('%d/%m/%Y %H:%M'))
#
#
# data_ora_ro()
#
#
# def data_ora_ch():
#     fus_china = pytz.timezone('Asia/Shanghai')
#     china = datetime.now(fus_china)
#     print('Data/Ora China: ', china.strftime('%d/%m/%Y %H:%M'))
#
#
# data_ora_ch()


# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)

# from datetime import date
#
#
# def zile_pana_la_onomastica():
#     data_curenta = date.today()
#     data_onomastica = date(date.today().year, 9, 26)
#     zile_ramase = (data_onomastica - data_curenta).days
#     print(f'Pana la ziua mea mai sunt {zile_ramase} zile')
#
#
# zile_pana_la_onomastica()