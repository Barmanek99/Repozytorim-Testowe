print('Sprawdzanie liczb parzystych niepodzielnych przez 3: ')
zakres_min=int(input('Podaj dolna granice zakresu: '))
zakres_max=int(input('Podaj gorna granice zakresu: '))
print('Zakres od '+str(zakres_min)+' do '+str(zakres_max))
print('Liczby spelniajace kryteria')
for i in range(zakres_min,zakres_max+1):
    if i%2==0 and i%3!=0:
        print(i)
