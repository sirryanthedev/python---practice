# (ex. 5.4.)

def bereken_deling(a: float, b: float) -> float:
        try:
            return a/b
        except ZeroDivisionError:
            print("Error: Je mag niet delen door nul!")
        except TypeError:
            print("Error: Argumenten moeten van het type float zijn!")
        except:
            print("Error: Er liep iets mis...")

while True:
    try:
        a = float(input("Geef een waarde voor het deeltal: "))
        b = float(input("Geef een waarde voor de deler: "))
    except:
        print("Error: Er wordt een getal als invoer verwacht, probeer het opnieuw...")

    else:
        if bereken_deling(a,b) != None:
            print(bereken_deling(a,b))
            break