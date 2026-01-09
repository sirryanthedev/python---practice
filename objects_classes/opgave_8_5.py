from __future__ import annotations

KLEUR = ["harten", "Schoppen", "Klaveren", "Ruiten"]
RANG = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas"]

class Kaart:
    def __init__(self, kleur: int, rang: int) -> None:
        self.kleur = kleur # index in KLEUR list
        self.rang = rang # index in RANG list

    def __str__(self):
        return "kleur: {} - rang: {}".format(KLEUR[self.kleur], RANG[self.rang])

    def __lt__(self, andere_kaart: Kaart):
        if self.rang != andere_kaart.rang:
            return self.rang < andere_kaart.rang
        return self.kleur < andere_kaart.kleur

# test
# print(Kaart(2,2))
# print(Kaart(2,4) < Kaart(2,3))
# print(Kaart(3,2) < Kaart(4,2))