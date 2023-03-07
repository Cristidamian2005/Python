# ''' 2 - Variabila de tip String - o variabila care poate contine unul sau mai multe caractere
#
#     4 - Declarare si initializare variabile:
# '''



# # xxxxxxxxxxxxxxxx   3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.   xxxxxxxxxxxxxxxxx
# marca = 'dacia'
# print(f'Variabila marca este de tip {type(marca)}')
# numar_intreg = 75
# print(f'Variabila numar_intreg este de tip {type(numar_intreg)}')
# #float
# pret = 8200.50
# print(f'Variabila pret este de tip {type(pret)}')
# #boolean
# inmatriculata = True
# print(f'Variabila inmatriculata este de tip {type(inmatriculata)}')


# # 4.  xxxxxxxxxxxxxxxx Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în  xxxxxxxxxxxxxxx
# # aceeași variabilă (suprascriere):
# # - Verifică tipul acesteia.
#
# pret = round(pret)
# print(f' Pretul rotuunjit este {pret}')
# assert type(pret)==int
# print('Rotunjire cu succes')
# if type(pret)==int:
#     print('rotunjire cu succes')
# else:
#     print('rotunjire fara succes')




# #  xxxxxxxxxxxxx5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.xxxxxxxxxxxx
#
# marca = 'dacia'
# print(f'Variabila marca este  {marca}')
# numar_intreg = 75
# print(f'Variabila numar_intreg  este  {numar_intreg}')
# #float
# pret = 8200.50
# print(f'Variabila pret  este  {pret}')
# #boolean
# inmatriculata = True
# print(f'Variabila inmatriculata  este  {inmatriculata}')




# # 6. xxxxxxxxxxxxxxxxxxxxxxxxxxxxCitește de la tastatură:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# # - numele;
# # - prenumele.
# # Afișează: 'Numele complet are x caractere'.
#
# # nume = input('Alege un nume ')
# # prenume = input('Alege un prenume ')
# # nume_complet = nume + ' ' + prenume
# #
# # print(f'Numele complet este {nume_complet} si are {len(nume_complet)} caractere')



# ############################## 7. Citește de la tastatură: ##############################
# # - lungimea;
# # - lățimea.
# #  Afișează: 'Aria dreptunghiului este x'.
#
# lungimea = float(input('Lungime = '))
# latimea = float(input('latimea = '))
# print(f'Aria dreptunghiului este {lungimea * latimea} ')




# 8. xxxxxxxxxxxxxxxxxxxxxx Având stringul: 'Coral is either the stupidest animal or the smartest rock': xxxxxxxxxxx
#
# - afișează de câte ori apare cuvântul 'the';

# text = 'Coral is either the stupidest animal or the smartest rock'
# print(f' Cuvantul \"the\" apare de {text.count("the")} ori')    ->gresit

# text = 'Coral is either the stupidest animal or the smartest rock'
# cuvant_the=text.split()
# print(f' Cuvantul \"the\" apare de {cuvant_the.count( "the")} ori')



# 9. xxxxxxxxxxxxxxxxxxxxxx inlocuieste cuvantul "the" cu "THE" xxxxxxxxxxxxxxxxxxxx
# text = 'Coral is either the stupidest animal or the smartest rock'
# cuvant_the=text.split()
# for i in range(len(cuvant_the)):
#
#     if cuvant_the[i] == 'the':
#         cuvant_the[i] = 'THE'
# print(' '.join(cuvant_the))


#
# ################ 10. Același string.Folosiți un assert ca să verificați dacă acest string conține doar numere.########
# text = 'Coral is either the stupidest animal or the smartest rock'
# assert text.isdigit() == False, "Acest text contine numere! "
# print('Am trecut de assert, textul contine doar litere! ')



# xxxxxxxxxxxxxxxxExerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai xxxxxxxxxxx
# nevoie de Google).

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx 1. Exercițiu: xxxxxxxxxxxxxxxxxxxxx
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.

#
# impar = input(" Introduceti un string de dimensiune impara: ")
# # verificari print(len(impar))
# # verificari print (int(len(impar)/2))
# if (len(impar)/2 != 0):
#     print(f' Caracterul din mijloc este: {impar[int(len(impar)/2) : int(len(impar)/2 +1) ] }')
# else:
#     print('String de dimensiune para')


# xxxxxxxxxxxxxxxxxx2. Folosind assert, verifică dacă un string este palindrom. xxxxxxxxxxxxxxxxxxx
#
# text = input('Introdu stringul: ')
# # print(text[0:3])
# # print(text[0:5])
# # print(text[0:5:-1])
# # verificari print(text[0:(int(len(text)/2))])
# # verificari print(text[-1 : -abs(int(len(text)/2+1)):-1])
# assert text[0:(int(len(text)/2))] == text[-1 : -abs(int(len(text)/2+1)):-1] , 'Stringul nu este palidrom'
# print('Stringul este palidrom')


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 3. Folosind o singură linie de cod : xxxxxxxxxxxxxxxxxxxxxxxxxxx
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

# varianta 1 nu stiu cat de corecta e
# a, b = input('baga primul cuvant '), input('baga al 2-lea cuvant ' )
# print(a)
# print(b)

#varianta 2 - si cea corecta cred

# stringu = input('baga stringu din 2 cuvinte ')
# cuv1, cuv2 = stringu.split()
# print(cuv1, cuv2 )

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  4. Exercițiu: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

# nope, nu merge
# stringu1 = str(input('Baga stringu '))
# prima_l = stringu1[0]
# print(prima_l)
# for i in range(1, (len(stringu1)-1)):
#     if prima_l == stringu1[i]:
#         stringu1[i] = stringu1[i].upper()
# print (stringu1)

# #asta merge
# stringu = input("Baga stringu ")
# prima_l = stringu[0]
# string_up = prima_l + stringu[1:-1].replace(prima_l, prima_l.upper()) + stringu[-1]
# print(f' Noul string este {string_up}')



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  5.Exercițiu:  xxxxxxxxxxxxxxxxxxxxxxxxx
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

# user, parola = input('Baga user '), input('Baga parola ')
# print(f"Parola pt user {user} este {'*' * len(parola)} si are {len(parola)} caractere.")


















# int i;
# for (i=1; i<20; i = i+3)
# System.out.println( i );

# for i in range(1, 20, 3):
#     print(i)
