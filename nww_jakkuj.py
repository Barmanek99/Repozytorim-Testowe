a = int(input('Wpisz pierwszą liczbę: '))
b = int(input('Wpisz drugą liczbę: '))
a1 = a
b1 = b
while b != 0:
    c = a
    d = b
    a = b
    b = c % d
e = a1*b1/a
print(int(e))
