# (ex. 8_2)

class Punt:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class Rechthoek:
    def __init__(self, punt, breedte=0.0, hoogte=0.0):
        self.punt = punt
        self.breedte = breedte
        self.hoogte = hoogte
        if not isinstance(breedte, (float, int)) or breedte < 0:
            self.breedte = 0.0
        if not isinstance(hoogte, (float, int)) or hoogte < 0:
            self.hoogte = 0.0

    def __repr__(self):
        return "[{}, b = {}, h = {}]".format(self.punt, self.breedte, self.hoogte)

    def oppervlakte(self):
        return self.breedte * self.hoogte

    def omtrek(self):
        return (self.hoogte + self.breedte) * 2

    def rechteronderhoek(self):
        rohoek = Punt(self.punt.x, self.punt.y)
        rohoek.x += self.breedte
        rohoek.y -= self.hoogte
        return rohoek

    @staticmethod # staticmethod because theres no implicit first argument: self
    def overlappend(r1: Rechthoek, r2: Rechthoek):
        if not isinstance(r1, Rechthoek) or not isinstance(r2, Rechthoek):
            return None
        x_links = max(r1.punt.x, r2.punt.x)
        x_rechts = min(r1.punt.x + r1.breedte, r2.punt.x + r2.breedte)
        y_boven = min(r1.punt.y, r2.punt.y)
        y_onder = max(r1.punt.y - r1.hoogte, r2.punt.y - r2.hoogte)
        if x_rechts <= x_links or y_onder >= y_boven:
            return None
        return Rechthoek(Punt(x_links, y_boven), x_rechts - x_links, y_boven - y_onder)

# tests with an example
# p = Punt(2,5)
# rhoek = Rechthoek(p, 2, 8)

# print(rhoek)
# print(rhoek.oppervlakte())
# print(rhoek.omtrek())
# print(rhoek.rechteronderhoek())