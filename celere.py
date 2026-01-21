import math

datum = input("Zadaj dátum (v tvare DD.MM.YYYY): ")
casti = datum.split(".")
den = int(casti[0])
mesiac = int(casti[1])
rok = int(casti[2])

if mesiac < 3:
    mesiac += 12
    rok -= 1
K = rok % 100
J = rok // 100
h = (den + math.floor(13 * (mesiac + 1) / 5) + K + math.floor(K / 4) + math.floor(J / 4) - 2 * J) % 7
dni = ["Sobota", "Nedeľa", "Pondelok", "Utorok", "Streda", "Štvrtok", "Piatok"]
print(dni[h])
