# (ex. 5.2.)

numlist = [100, 101, 0, "103", 104]

try:
    i1 = int(input("Geef een index: "))
    print("100 /", numlist[i1], "=", 100 / numlist[i1])
except ZeroDivisionError:
    print("Error: Je kan niet delen door nul!")
except IndexError:
    print(f"Error: De hoogste index is 4, jouw invoer: {i1}")
except TypeError:
    print("Error: Je kan een geheel getal (int) niet delen door een string")
except:
    print("Error: Er liep iets mis...")