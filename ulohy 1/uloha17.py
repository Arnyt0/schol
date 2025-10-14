cislo = int(input("Zadaj číslo: "))

delitel = 2
print("Prvočíselný rozklad:", end=" ")

while delitel * delitel <= cislo:
    while cislo % delitel == 0:
        print(delitel, end=" ")
        cislo //= delitel
    delitel += 1

if cislo > 1:
    print(cislo)
else:
    print()
