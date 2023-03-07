# 1. Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
import random

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')

# i=0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1


# 2. Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if i == 0 or i == (len(masini)-1):
#         continue
#     masini[i] = masini[i].upper()
# else:
#     print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == "Mercedes":
#         print('Am gasit masina dorita de dvs')
#         break
# else:
#     print('Nu am gasit masina cautata de Dvs')
#

## Am facut si o varianta cu input de la utilizator
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masina_cautata = ''
# da_nu = 'da'
# while da_nu != 'nu' and masina_cautata not in masini :
#     masina_cautata = input('Ce masina vrei mare Boss ce esti? Baga aici, daca stii sa scrii: ')
#     for masina in masini:
#         if masina == masina_cautata:
#             print(f'Am gasit masina dorita de dvs, si anume {masina_cautata}')
#             break
#     else:
#         print('Nu am gasit masina cautata de Dvs')
#         da_nu = input('Mai cautam sefu? da/nu: ')


# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_naspa = ['Lastun', 'Trabant']
# for masina in masini:
#     if masina in masini_naspa:
#         continue
#     else:
#         print(f'S-ar putea sa va placa masina {masina}')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#
# ● Printează Modele vechi: x.
# ● Modele noi: x.

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# print(masini)
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Lastun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = "Tesla"
# print(f'Masini vechi: {masini_vechi}')
# print(f'Masini noi: {masini}')


# 6. Având dict:
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# buget = 15000
# for masina, pret in pret_masini.items():
#     if buget >= pret:
#         print(f"Pentru un buget de sub {buget} euro puteți alege mașina {masina}")
# for masina, pret in pret_masini.items():
#     print(f'Masina {masina} are pretul {pret}')


# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

# i = 0
# trei = 0
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# while i < len(numere):
#     print(numere[i])
#     if numere[i] == 3:
#         trei += 1
#     i += 1
# print(f'Cifra 3 apare de {trei} ori')


# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for i in range(len(numere)):
#     suma += numere[i]
# print(f'Suma este {suma}')


# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max = numere[0]
# for i in range(len(numere)):
#     if numere[i] > max:
#         max = numere[i]
# print(max)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in range(len(numere)):
#     numere[i] = -abs(numere[i])
# print(numere)


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
# Google.
# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar < 0:
#         numere_negative.append(numar)
#     else:
#         numere_pozitive.append(numar)
# print(f'Alte numere: {alte_numere}')
# print(f'Numere pare: {numere_pare}')
# print(f'Numere impare: {numere_impare}')
# print(f'Numere pozitive: {numere_pozitive}')
# print(f'Numere negative: {numere_negative}')


# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# print(alte_numere)
# n = len(alte_numere)
# swapped = False
# for i in range(n-1):
#     for j in range(0, n - i - 1):
#         if alte_numere[j] > alte_numere[j + 1]:
#             swapped = True
#             alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
#     if not swapped:
#         break
# print(alte_numere)


# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

# numar_secret = random.randint(1,30)
# numar_ghicit = None
# while numar_secret != numar_ghicit:
#     numar_ghicit = int(input("Alege un numar intre 1 si 30: "))
#     if numar_ghicit > numar_secret:
#         print('Numar secret e mai mic')
#     elif numar_ghicit < numar_secret:
#         print('Numar secret e mai mare')
#     else:
#         print(f'Ai ghicit, numarul secret era: {numar_secret}')

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

# numar = int(input('Introdu numarul: '))
# for i in range(1, numar+1):
#     for j in range(i):
#         print(f'{i}', end="")
#     print('')

# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)


# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
#
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print(f'Cifra curenta este: {tastatura_telefon[i][j]}')
#
#
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print(tastatura_telefon[i][j], ' ', end='')
#     print('')

