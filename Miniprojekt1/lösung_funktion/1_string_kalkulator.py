import math


def addiere(a, b):
    return a + b


def subtrahiere(a, b):
    return a - b


def multipliziere(a, b):
    return a * b


def dividiere(a, b):
    if b == 0:
        return "Fehler: Division durch 0"
    return a / b


def wurzel(a):
    return math.sqrt(a)


def betrag(a):
    return abs(a)


def runden_auf(a):
    return math.ceil(a)


def rechner(eingabe):
    eingabe = eingabe.lower().strip()

    if " + " in eingabe:
        teile = eingabe.split(" + ")
        a = float(teile[0])
        b = float(teile[1])
        return addiere(a, b)

    elif " - " in eingabe:
        teile = eingabe.split(" - ")
        a = float(teile[0])
        b = float(teile[1])
        return subtrahiere(a, b)

    elif " * " in eingabe:
        teile = eingabe.split(" * ")
        a = float(teile[0])
        b = float(teile[1])
        return multipliziere(a, b)

    elif " / " in eingabe:
        teile = eingabe.split(" / ")
        a = float(teile[0])
        b = float(teile[1])
        return dividiere(a, b)

    elif "wurzel von" in eingabe:
        a = float(eingabe.replace("wurzel von", ""))
        return wurzel(a)

    elif "betrag von" in eingabe:
        a = float(eingabe.replace("betrag von", ""))
        return betrag(a)

    elif "ceil von" in eingabe or "runden auf" in eingabe:
        a = float(eingabe.replace("ceil von", "").replace("runden auf", ""))
        return runden_auf(a)

    else:
        return "Fehler: Eingabe nicht erkannt"


# Testbeispiele
print(rechner("10 + 5"))  # 15.0
print(rechner("Wurzel von 64"))  # 8.0
print(rechner("Ceil von 3.2"))  # 4
print(rechner("Betrag von -7"))  # 7
print(rechner("20 / 0"))  # Fehler
print(rechner("20 / 4"))
print(rechner("20 + 4"))
