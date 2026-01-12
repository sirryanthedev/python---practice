def aantal_voorkomens(edities: Edities) -> dict[Nummer, int]:
    nummer_count = {}
    for editie in edities.values():
        for nummer in editie:
            nummer_count[nummer] = nummer_count.get(nummer, 0) + 1
    return nummer_count

def eenjaarsvliegen(edities: Edities) -> list[Nummer]:
    base = []
    eenjaarsvliegen = set()

    for nummers in edities.values():
        base.append(nummers)
    for index, nummers in enumerate(base):
        for nummer in nummers:
            # initialise flags
            not_in_previous = False
            not_in_next = False

            if index == 0: # edge case: nummer in first list (value) is not in previous value, since it doesn't exist
                not_in_previous = True
            if index == len(base) - 1: # edge case: nummer in last list (value) is not in next value, since it doesn't exist
                not_in_next = True

            if index > 0: # there's a previous list, therefore we can do the check accordingly
                if nummer not in base[index - 1]:
                    not_in_previous = True
            if index < len(base) - 1: # there's a next list, therefore we can do the check accordingly
                if nummer not in base[index + 1]:
                    not_in_next = True

            if not_in_previous and not_in_next:
                eenjaarsvliegen.add(nummer)
    return list(eenjaarsvliegen)

def definitieve_eenjaarsvliegen(edities: Edities) -> list[Nummer]:
    eenjaarsvliegen_list = eenjaarsvliegen(edities)
    voorkomens_list = aantal_voorkomens(edities)
    definitieve_eenjaarsvliegen = set()
    for nummer in eenjaarsvliegen_list:
        if voorkomens_list[nummer] == 1:
            definitieve_eenjaarsvliegen.add(nummer)
    return list(definitieve_eenjaarsvliegen)