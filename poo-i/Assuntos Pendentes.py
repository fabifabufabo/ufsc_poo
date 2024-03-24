

assuntos = input()

pendencias = 0

for assunto in assuntos:

    if assunto == "(":
        pendencias += 1

    elif assunto == ")" and pendencias > 0:
        pendencias -= 1

if pendencias > 0:

    print(f"Ainda temos {pendencias} assunto(s) pendente(s)!")

else:

    print("Partiu RU!")
