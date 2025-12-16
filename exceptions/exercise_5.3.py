# (ex. 5.3.)

import math

def bereken_wortel(getal: float) -> float:
    try:
        return math.sqrt(getal)
    except ValueError:
        print("Error: Het getal moet positief zijn...")
    except TypeError:
        print("Error: Argument moet van type int zijn...")
    except:
        print("Error: Er liep iets mis...")