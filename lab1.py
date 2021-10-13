# zad1
from re import match
from unittest import case

print("zadanie1: ")


def funkcja1(imie, nazwisko):
    return print(imie + "." + nazwisko)


print(funkcja1("T", "Mastyka"))
print("=================")

# zad2
print("zadanie2: ")


def funkcja2(imie, nazwisko):
    return (print(imie[0].capitalize() + "." + nazwisko.capitalize()))


print(funkcja2("Tomasz", "Mastyka"))
print("=================")

# zad3
print("zadanie 3: ")


def funkcja3(a, b, c):
    rok_aktualny = a + b
    d_urodzenia = int(rok_aktualny) - c
    return print(d_urodzenia)


print(funkcja3("20", "21", 18))
print("=================")
# zad 4
print("zadanie 4: ")


def funkcja4(imie, nazwisko, funkcja2):
    return print(funkcja2(imie, nazwisko))


print(funkcja4("Tomasz", "Mastyka", funkcja2))
print("=================")

# zad 5
print("zadanie 5: ")


def funkcja5(a, b):
    if ((a & b > 0) & (b != 0)):
        return a / b


print(funkcja5(10, 2))
print("=================")

# # zad 6
# print("zadanie 6: ")
#
#
# def funkcja6():
#     licznik = 0
#     while licznik <= 99:
#         liczba = int(input("Podaj liczbe, ktora chcesz dodac: ))
#         licznik += liczba
#
#
# print(funkcja6())
# print("=================")

# zad 7
print("zadanie 7: ")
lista1 = ["irek", "maciek", "pawel"]
print(lista1)


def funkcja7(lista):
    krotka = tuple(lista)
    return (krotka)


print(funkcja7(lista1))
print("=================")

# # zad 8
# print("zadanie 8: ")
#
#
# def funkcja8():
#     lista2 = []
#     for x in range(3):
#         lista2.append(input("podaj wartosc, ktora chcesz dodac do listy: "))
#     krotka2 = tuple(lista2)
#     return krotka2
#
#
# print(funkcja8())
# print("=================")

# zad 9
print("zadanie 9: ")


def funkcja9(numer):
    dopasowania = {1: "poniedzialek", 2: "wtorek", 3: "sroda", 4: "czwartek", 5: "piatek", 6: "sobota",
                   7: "niedziela"}
    zwrot = dopasowania.get(numer)
    return print(zwrot)


print(funkcja9(4))

# zad 10
print("zadanie 10: ")


def funkcja10(wyraz):
    if (wyraz == wyraz[::-1]):
        return True
    else:
        return False


print(funkcja10("kajak"))
