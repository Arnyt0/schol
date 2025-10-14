cislo = int(input("Zadaj číslo: "))

if cislo < 2:
    print("Číslo nie je prvočíslo.")
else:
    delitel = 2
    je_prvocislo = True
    while delitel * delitel <= cislo:
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 1

    if je_prvocislo:
        print("Číslo je prvočíslo.")
    else:
        print("Číslo nie je prvočíslo.")
