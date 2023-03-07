# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

# if (conditia se indeplineste) executa (codul asta)
# else executa (codu asta)


# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)

# numar = input('Introdu numarul ')
# if numar.isnumeric() and numar.isdigit() :
#     print('Numar natural')
# else :
#     print(" Nu e numar natural ")


# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

# numar = float(input('Introdu numarul '))
# if numar < 0 :
#     print (' Esti negativist boss ')
# elif numar > 0 :
#     print(' Esti pozitivist boss')
# else :
#     print(' Esti neutralist boss')


# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

# numar = float(input('Introdu numarul '))
# if numar >= -2 and numar <= 13 :
#     print(f' Numarul {numar} este in intervalul -2 : 13 ')
# else:
#     print(f' Numarul {numar}  NU este in intervalul -2 : 13 ')


# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs

# !!! am inteles bine enuntul ?


# x = int(input('X = '))
# y = int(input('Y = '))
# print(abs(abs(x) - abs(y)) - 1)
# if (abs(abs(x) - abs(y)) - 1) < 5 :
#     print(f'Diferenta dintre x si y este mai mica de 5 si anume {abs(abs(x) - abs(y)) - 1} numere')
# else :
#     print(f'Diferenta dintre x si y este mai mare sau egala cu 5 si anume {abs(abs(x) - abs(y)) - 1} numere')
#


# 6 Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

# numar = int(input('Introdu numarul '))
# if not (numar >= 5 and numar <= 27) :
#     print(f' Numarul {numar} NU este in intervalul 5 : 27 ')
# else:
#     print(f' Numarul {numar} este in intervalul 5 : 27 ')


# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare

# x = int(input('X = '))
# y = int(input('Y = '))
# if x == y :
#     print(' Numerele sunt egale ')
# else :
#     if x > y :
#         print(' X e mai mare')
#     else:
#         print(' Y e mai mare')



# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

# x = int(input('X = '))
# y = int(input('Y = '))
# z = int(input('Z = '))
#
# if x == y == z :
#     print('Triunghi echilateral')
# elif x == y or x == z or y == z :
#     print('Triunghi isoscel')
# else :
#     print('Triunghi oarecare')



# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# litera_citita = input('Itroduceti litera: ')
# # vocale = a e i o u
# assert litera_citita.isalpha() == True,  'Caracterul citit nu este litera'
# if litera_citita =='a' or (litera_citita=='A') or litera_citita =='e' or (litera_citita=='E') or  litera_citita =='i' or (litera_citita=='I') or  litera_citita =='o' or (litera_citita=='O') or  litera_citita =='u' or (litera_citita=='U'):
#     print('Litera citita este vocala! ')
# else:
#     print('Litera citita este consoana! ')



# litera_citita = input('Itroduceti litera: ')
# # vocale = a e i o u
# if litera_citita.lower() in 'aeiou' and litera_citita.isalpha():
#     print('vocala')
# elif not litera_citita.isalpha():
#     print('nu e litera')
# else:
#     print('consoana')


# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F

# nota = float(input(' Baga nota sefu! : '))
# if nota > 9 :
#     print(' Ai luat A ')
# elif nota > 8 :
#     print('Ai luat B ')
# elif nota > 7 :
#     print('Ai luat C ')
# elif nota > 6 :
#     print('Ai luat D ')
# elif nota > 4 :
#     print('Ai luat E ')
# else:
#     print('Ne vedem la vara patroane! Ai luat F :))')

######### Optionale ###########

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

# x = int(input('Baga X-ul : '))
# if len(str(x)) >= 4 :
#     print('Are minim 4 cifre')
# else :
#     print('Are mai putin de 4 cifre')

# 2. Verifica daca x are exact 6 cifre

# x = int(input('Baga X-ul : '))
# if len(str(x)) == 6 :
#     print('Are 6 cifre')
# else :
#     print('Nu are 6 cifre ')

# 3. Verifica daca x este numar par sau impar

# x = int(input('Baga X-ul : '))
# if x % 2 == 0 :
#     print('Par')
# else :
#     print('Impar')


# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele

# nu am tratat cazurile in care doua din ele sunt egale

# x, y, z = int(input('Baga X ')), int(input('Baga Y ')), int(input('Baga Z '))
# if (x > y) and (x > z) :
#     print(' X e sefu cel mare ')
# elif (y > z) and (y > x) :
#     print(' Y e sefu cel mare ')
# elif (z > y) and (z > x) :
#     print(' Z e sefu cel mare ')
# elif (x == y == z) :
#     print('Sunt trei sefi si nici un muncitor :)) ')
# elif (x == y) and (x > z):
#     print(' Sefu X si sefutu Y sunt patroni, Z e muncitor')
# elif (x == z) and (x > y):
#     print(' Sefu X si sefutu Z sunt patroni, Y e muncitor')
# elif (y == z) and (y > x):
#     print(' Sefu Y si sefutu Z sunt patroni, X e muncitor')
# elif (x == y) and (x < z):
#     print(' Z e sefu cel mare')
# elif (x == z) and (x < y):
#     print(' Y e sefu cel mare')
# elif (y == z) and (y < x):
#     print(' X e sefu cel mare ')



# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# lungimea celei de-a treia laturi)

# x, y, z = int(input('Baga X ')), int(input('Baga Y ')), int(input('Baga Z '))
# if x + y + z == 180 :
#     print('Ai nimerit, ai un triunghi')
# elif ((x + y) > z) and ((x + z) > y) and ((z + y) > x) :
#     print(" triunghi")
# else :
#     print(' nu e triunghi')




# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'

# stringul = 'Coral is either the stupidest animal or the smartest rock'
# numar = int(input(' Baga numaru: '))
# print(stringul[:(len(stringul)-numar):])
# print(stringul[:-numar:])
# #am printat si invers hahahahaha
# print(stringul[::-1])


# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5

# stringul = 'Coral is either the stupidest animal or the smartest rock'
# string_nou = stringul[:5:] + stringul[-5::]
# print(string_nou)
# string_nou = stringul[:6:] + stringul[-6::]
# print(string_nou)

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '

# stringul = 'Coral is either the stupidest animal or the smartest rock'
# poz_rock = stringul.index('rock')
# print(stringul[:poz_rock:])


# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)

# stringu = str(input(' Baga stringu Boss! '))
# stringu_insensibil = stringu.lower()
# assert stringu_insensibil[:1:] == stringu_insensibil [-1::] , 'Nu sunt identice'
# print('Sunt la fel')

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

# stringul = '0123456789'
# print(f' Numerele pare {stringul[::2]}')
# print(f' Numerele impare {stringul[1::2]}')


########### Bonus ##########

# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
# inputuri urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
# si are permisiune in scris de la celalat parinte
#
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
# variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
# apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca



# incercare abandonata cu functie, facem cu IF-uri ca tot suntem la lectia cu IF :)) vezi mai jos.
# Poate ne explici pe scurt cum o gandesti cu o functie la inceputul cursului

# def verificare (varsta, pasaport, ins_m, ins_t, bil_m, bil_t) :
#     if varsta >= 18 and pasaport :
#         return True
#     elif pasaport and ins_m and ins_t :
#         return True
#     elif (pasaport and ins_m and bil_t) or (pasaport and ins_t and bil_m) :
#         return True
#     else :
#         return False
#
# varsta = int(input('varsta '))
# pasaport =input('Are pasaport? D/N ')
# if pasaport == 'D' :
#     pasaport = True
# elif pasaport == 'N':
#     pasaport = True
# else :
#     print('Esti incoerent amice')
#
#
# print(verificare(varsta, pasaport, False, False, False, False))


############ Varianta cu IF-uri
#
# varsta = int(input("Ce varsta are pasagerul? Va rugam rotunjiti la varsta implinita. Introdu varsta acum: "))
# pasaport = int(input("Pasagerul are pasaport? Apasa 1 daca DA sau 0 daca NU. Apasa: "))
# ins_mama = int(input("Pasagerul este insotit de mama? Apasa 1 daca DA sau 0 daca NU. Apasa: "))
# ins_tata = int(input("Pasagerul este insotit de tata? Apasa 1 daca DA sau 0 daca NU. Apasa: "))
# act_mama = int(input("Pasagerul are actul de permisiune de la mama? Apasa 1 daca DA sau 0 daca NU. Apasa: "))
# act_tata = int(input("Pasagerul are actul de permisiune de la tata? Apasa 1 daca DA sau 0 daca NU. Apasa: "))

# imbarcat = 0
# if varsta >= 18 and pasaport == 1 :
#     imbarcat += 1
# elif varsta < 18 and pasaport == 1 and ins_mama == 1 and ins_tata == 1 :
#     imbarcat += 1
# elif varsta < 18 and pasaport == 1 and ins_mama == 1 and act_tata == 1 :
#     imbarcat += 1
# elif varsta < 18 and pasaport == 1 and ins_tata == 1 and act_mama == 1:
#     imbarcat += 1
#
# if imbarcat == 0 :
#     print("Imbarcare respinsa")
#
# else :
#     print("Imbarcare acceptata")


#
# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# - Verifica si afiseaza daca utilizatorul a ghicit numarul
# - Vor exista 3 optiuni care vor trebui tratate:
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari? Ai ales x si zarul a fost y

# import random
# dice_roll = random.randint(1,6)
# print(dice_roll)
# ales = int(input(' Alege un numar intre 1 si 6 bosulica: '))
# if ales == dice_roll :
#     print(f"Cine-i barosanu ? Cine, cine? Tu esti sefule, ai ales {ales} si zarul a fost {dice_roll} !")
# elif ales < dice_roll :
#     print(f"Cine-i barosanu ? Cine, cine? NU esti tu, ai ales un numar mai mic. Ai ales {ales} si zarul a fost {dice_roll} !")
# else:
#     print(f"Cine-i barosanu ? Cine, cine? NU esti tu, ai ales un numar mai mare. Ai ales {ales} si zarul a fost {dice_roll} !")








