# --- KLASSENDEFINITIONEN ---

# Basisklasse für alle Kontotypen
class Konto:
    def __init__(self, kontonummer, anfangsguthaben=0):
        self.kontonummer = kontonummer
        self.saldo = anfangsguthaben

    def einzahlen(self, betrag):
        if betrag > 0:
            self.saldo += betrag

    def abheben(self, betrag):
        if 0 < betrag <= self.saldo:
            self.saldo -= betrag
            return True
        return False

    def kontostand(self):
        return self.saldo


# Sparkonto mit Zinssatz
class Sparkonto(Konto):
    def __init__(self, kontonummer, anfangsguthaben=0, zinssatz=0.02):
        super().__init__(kontonummer, anfangsguthaben)
        self.zinssatz = zinssatz

    def zinsen_hinzufuegen(self):
        zinsen = self.saldo * self.zinssatz
        self.saldo += zinsen

# Girokonto mit Überziehungslimit
class Girokonto(Konto):
    def __init__(self, kontonummer, anfangsguthaben=0, ueberziehungslimit=0):
        super().__init__(kontonummer, anfangsguthaben)
        self.ueberziehungslimit = ueberziehungslimit

    def abheben(self, betrag):
        if betrag <= self.saldo + self.ueberziehungslimit:
            self.saldo -= betrag
            return True
        return False

# Klasse für Bankkunden
class Kunde:
    def __init__(self, name, kundennr):
        self.name = name
        self.kundennr = kundennr
        self.konten = []

    def konto_hinzufuegen(self, konto):
        self.konten.append(konto)

    def konto_entfernen(self, konto):
        if konto in self.konten:
            self.konten.remove(konto)

    def konten_auflisten(self):
        print(f"Konten von {self.name}:")
        for konto in self.konten:
            typ = type(konto).__name__
            print(f"- {typ} ({konto.kontonummer}): €{konto.kontostand():.2f}")

# Klasse für die Bank selbst (verwaltet Kunden)
class Bank:
    def __init__(self):
        self.kunden = []

    def kunde_hinzufuegen(self, kunde):
        self.kunden.append(kunde)

    def kunde_entfernen(self, kunde):
        if kunde in self.kunden:
            self.kunden.remove(kunde)


# --- TESTSZENARIO / ANWENDUNG ---

# Kunde Alice wird erstellt
alice = Kunde("Alice", "C001")

# Sparkonto und Girokonto für Alice erstellen
sparkonto = Sparkonto("S100", 1000, 0.02)
girokonto = Girokonto("G200", 500, 200)

# Konten zu Alice hinzufügen
alice.konto_hinzufuegen(sparkonto)
alice.konto_hinzufuegen(girokonto)

# Transaktionen durchführen
sparkonto.einzahlen(200)         # Sparkonto: 1000 + 200 = 1200
girokonto.abheben(300)          # Girokonto: 500 - 300 = 200

# Versuch, 800 € abzuheben (soll fehlschlagen, da über dem Limit)
abhebung_erlaubt = girokonto.abheben(800)

# Zinsen für Sparkonto berechnen
sparkonto.zinsen_hinzufuegen()

# Kontenübersicht anzeigen
print("\n--- Übersicht vor Kontoschließung ---")
alice.konten_auflisten()

# Girokonto wird geschlossen
alice.konto_entfernen(girokonto)

# --- AUSGABE ---

print("\nErgebnisse:\n")

print("1. Sparkonto-Saldo nach Einzahlung & Zinsen: €", round(sparkonto.kontostand(), 2))
print("2. War die 800€-Abhebung erlaubt?", abhebung_erlaubt)
print("3. Girokonto noch vorhanden?", girokonto in alice.konten)


# alice.konten_auflisten()