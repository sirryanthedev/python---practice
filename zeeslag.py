# (ex. zeeslag - Dodona)

def boot_overlappend(set_1: set, set_2: set) -> bool:
    return not set_1.isdisjoint(set_2)

def boot_toevoegen(set_1: set, set_2: set) -> set:
    if not boot_overlappend(set_1, set_2):
        return set_1.union(set_2)
    return set_2

def vuur(str_1: str, set_2: set) -> tuple:
    a = str_1 in set_2
    if a:
        set_2.discard(str_1)
        return (a, set_2)
    return(a, set_2)

# Zeeslag wordt gespeeld op een veld van bijvoorbeeld 9 x 9 hokjes. Een hokje wordt aangeduid met een letter-cijfercombinatie, bijvoorbeeld A1 of B9. Iedere speler mag op zijn helft tien schepen plaatsen met, afhankelijk van de zeeslagvariant, een omvang variërend van 1 tot 6 opeenvolgende hokjes. Schepen mogen horizontaal of verticaal staan, maar niet diagonaal.

# Zeeslag
# De soorten en aantallen toegestane schepen zijn hetzelfde voor elke speler. Er bestaan heel wat varianten maar de meest gebruikte schepen zijn:

# vliegdekschip: 6 vakjes
# slagschip: 4 vakjes
# onderzeeër: 3 vakjes
# patrouilleschip: 2 vakjes
# Nadat de schepen zijn geplaatst, verloopt het spel in een aantal ronden. De spelers noemen om beurt een hokje in het rooster van de tegenstander. De tegenstander zegt 'geraakt' indien het vak wordt bezet door een schip. Om zich een beeld te vormen van de vloot van de tegenstander neemt de speler nota van de treffer of misser. Doel is om als eerste alle locaties van alle schepen van de tegenstander te raden en zo de vloot van de tegenstander tot zinken te brengen.

# In deze oefening wordt de ligging van de boten op het rooster bijghouden in een set. Ook een enkele boot wordt voorgesteld door een set van vakjes. Hieronder vind je de grijze vloot zoals in de afbeelding getoond.

# {'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}
# Opgave
# Programmeer volgende drie functies:

# De functie boot_overlappend gaat na of de boot in de eerste parameter overlapt met de boten in het rooster van de tweede parameter. Overlappen betekent minstens één vakje gemeenschappelijk hebben. Indien de boot met geen enkele boot overlapt, wordt er False teruggegeven. In het andere geval wordt True teruggegeven.

# boot_toevoegen voegt de boot in de eerste parameter toe aan het rooster in de tweede parameter indien de boot met geen enkele boot in het rooster overlapt. De functie geeft het rooster terug waaraan de niet-overlappende boot (niet) werd toegevoegd.

# De functie vuur controleert of het vakje in de eerste parameter in het rooster aangekruist werd. De functie geeft True terug indien dat het geval was, anders False. De functie geeft ook een eventuele update van het rooster terug waarin het aangekruist vakje geschrapt werd.

# In deze oefening kunnen boten aan elkaar grenzen.