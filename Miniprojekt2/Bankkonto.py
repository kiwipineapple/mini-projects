class Konto:
    def __init__(self, kontotype) -> None:
        self.kontotype = kontotype


class Kunde:
    def __init__(self, name) -> None:
        self.name = name

    def einzahlen(self, betrag):
        print(f'{betrag}')


class Bank:
