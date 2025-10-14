cislo = int(input("Zadaj číslo v desiatkovej sústave: "))

dvojkove = 0
nasobok = 1

while cislo > 0:
    posledna_cifra = cislo % 2
    dvojkove += posledna_cifra * nasobok
    nasobok *= 10
    cislo //= 2

print("Číslo v dvojkovej sústave je:", dvojkove)
