cislo = int(input("Zadaj číslo v dvojkovej sústave: "))

desiatkove = 0
nasobok = 1

while cislo > 0:
    posledna_cifra = cislo % 10
    desiatkove += posledna_cifra * nasobok
    nasobok *= 2
    cislo //= 10

print("Číslo v desiatkovej sústave je:", desiatkove)
