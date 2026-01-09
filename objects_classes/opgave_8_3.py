# (ex. 8_3)

class Student:
    def __init__(self, voornaam, achternaam, administratienummer):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.nummer = administratienummer
        self.inschrijvingen = []

    def inschrijven(self, cursus):
        if isinstance(cursus, Cursus) and cursus not in self.inschrijvingen:
            self.inschrijvingen.append(cursus)

class Cursus:
    def __init__(self, naam, nummer):
        self.naam = naam
        self.nummer = nummer

def toon_info(student_list: list[Student]):
    for student in student_list:
        if isinstance(student, Student):
            cursus_str = ", ".join(cursus.naam for cursus in student.inschrijvingen)
            print(f"{student.nummer} - {student.voornaam} - {student.achternaam} - {cursus_str}")

# tests
# eerste_cursus = Cursus("Algebra", 1)
# tweede_cursus = Cursus("Fysica", 2)
# derde_cursus = Cursus("Chemie", 3)
# vierde_cursus = Cursus("Biologie", 4)
# vijfde_cursus = Cursus("Calculus", 5)

# james = Student("James", "Pimblett", 2504458)
# ann = Student("Ann", "Beckhamm", 2521389)

# james.inschrijven(eerste_cursus)
# james.inschrijven(tweede_cursus)

# ann.inschrijven(vierde_cursus)
# ann.inschrijven(vijfde_cursus)

# toon_info([ann, james])