x = int(input("koniec cislo: "))
suma = 0
for i in range(1,x+1):
    if i%2==0:
        suma += i

print(suma)