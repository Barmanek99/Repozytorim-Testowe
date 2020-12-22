a=int(input('Wpisz pierwszą liczbę: '))
b=int(input('Wpisz drugą liczbę: '))
while(b != 0):
    c=a
    d=b
    a=b
    b=c%d
print(a)