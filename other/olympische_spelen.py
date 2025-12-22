# (ex. olympische spelen - Dodona)

def medailleOverzicht(info: list[tuple[str]], medal: str = "") -> dict:
    infodict = {}

    if medal == "gold":
        for tpl in info:
            if tpl[4] == "gold":
                infodict[tpl[0]] = infodict.get(tpl[0], 0) + 1

    elif medal == "silver":
        for tpl in info:
            if tpl[4] == "silver":
                infodict[tpl[0]] = infodict.get(tpl[0], 0) + 1
    elif medal == "bronze":
        for tpl in info:
            if tpl[4] == "bronze":
                infodict[tpl[0]] = infodict.get(tpl[0], 0) + 1
    else:
        for tpl in info:
            infodict[tpl[0]] = infodict.get(tpl[0], 0) + 1

    return infodict

def top(infodict: dict, n: int = 10) -> list[tuple]:
    if n > len(infodict):
        raise ValueError("n must be less than the length of the dictionairy!")
    sorted_list = [x for x in sorted(infodict.items(), key=lambda item: -item[1])]
    return sorted_list[:n]