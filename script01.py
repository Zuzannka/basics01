
print("Sztuczka magiczna, podaj 3 cyfry i ci wyrzuci coś niepspodzianka")
#input of numbers
num1 = input('Podaj pierwszą liczbę: ')
num2 = input('Podaj drugą liczbę: ')
num3 = input('Podaj trzecią liczbę:')
if num3 == '2':
#definition of 'sum'
    sum = float(num1) + float(num2)
    print ('oto twoja niemspodzianka, sume pierwszej i drugiej liczby',sum)
else:
#definition of 'dif'
    dif = float(num2) - float(num1)
    print('Oto twoja niepspodzianka, różnica drugiej i pierwszej liczby', dif)



