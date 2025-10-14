cislo = int(input("Zadaj prirodzené číslo: "))

sucet = 0

while cislo > 0:
    posledna_cifra = cislo % 10
    sucet += posledna_cifra
    cislo //= 10

print("Ciferný súčet je:", sucet)
