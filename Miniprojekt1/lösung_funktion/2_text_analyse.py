# Funktion: Wortanzahl zählen
def zaehle_woerter(text):
    woerter = text.split()
    return len(woerter)

# Funktion: Längstes Wort finden
def laengstes_wort(text):
    woerter = text.split()
    laengstes = ""
    for wort in woerter:
        if len(wort) > len(laengstes):
            laengstes = wort
    return laengstes

# Funktion: Durchschnittliche Wortlänge berechnen
def durchschnittliche_wortlaenge(text):
    woerter = text.split()
    gesamt = 0
    for wort in woerter:
        gesamt += len(wort)
    if len(woerter) == 0:
        return 0
    return gesamt / len(woerter)

# Funktion: Wörter alphabetisch sortieren
def alphabetisch_sortieren(text):
    woerter = text.split()
    return sorted(woerter)

# Funktion: Häufigstes Wort finden
def haeufigstes_wort(text):
    woerter = text.lower().split()
    zaehlung = {}
    for wort in woerter:
        if wort in zaehlung:
            zaehlung[wort] += 1
        else:
            zaehlung[wort] = 1

    haeufigstes = ""
    maximale_anzahl = 0
    for wort in zaehlung:
        if zaehlung[wort] > maximale_anzahl:
            haeufigstes = wort
            maximale_anzahl = zaehlung[wort]
    return haeufigstes, maximale_anzahl

# Funktion: Wortlängen-Verteilung
def wortlaengen_verteilung(text):
    woerter = text.split()
    verteilung = {}
    for wort in woerter:
        laenge = len(wort)
        if laenge in verteilung:
            verteilung[laenge] += 1
        else:
            verteilung[laenge] = 1
    return verteilung

# Hauptfunktion zur Zusammenfassung
def analysiere_text(text):
    ergebnis = ""

    ergebnis += "Anzahl der Wörter: " + str(zaehle_woerter(text)) + "\n"
    ergebnis += "Längstes Wort: " + laengstes_wort(text) + "\n"
    ergebnis += "Durchschnittliche Wortlänge: " + str(round(durchschnittliche_wortlaenge(text), 2)) + "\n"
    ergebnis += "Alphabetisch sortiert: " + ", ".join(alphabetisch_sortieren(text)) + "\n"

    wort, anzahl = haeufigstes_wort(text)
    ergebnis += "Häufigstes Wort: '" + wort + "' (kommt " + str(anzahl) + " mal vor)\n"

    ergebnis += "Wortlängen-Verteilung:\n"
    verteilung = wortlaengen_verteilung(text)
    for laenge in sorted(verteilung.keys()):
        ergebnis += f"  {laenge} Buchstaben: {verteilung[laenge]} Wörter\n"

    return ergebnis

# Beispieltext
text_item = "Python ist toll und Python macht Spaß und Lernen ist wichtig"
print(analysiere_text(text_item))
