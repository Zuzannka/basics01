print("Sztuczka magiczna, podaj 3 cyfry i ci wyrzuci coś niepspodzianka")
a = input('Podaj pierwszą liczbę:')
b = input('Podaj drugą liczbę:')
c = bool(int(input("by dodać wpisz 1, by odjąć wpisz 0: ")))
def funkcja(a,b,c):
    if c == False:
        sum = float(a) + float(b)
        print (sum)
    else:
        dif = float(a) - float(b)
        print (dif)
funkcja(a,b,c)