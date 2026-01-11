from stemmen_types import *
from tijdloze100_types import *
import csv, re

def bereken_top100(stemmenlijst: Stemmenlijst) -> Editie:
    """return a list of the top 100 votes, sorted in a unique way

    Args:
        stemmenlijst (Stemmenlijst): list where each item is an element of type Stem

    Returns:
        Editie: list where each item is an element of type Nummer - list[tuple[str, str, int])]
    """
    editie = []
    for item in stemmen_lijst:
        info = (item.nummer, item.timestamp)
        editie.append(info)

    nummer_info = {}
    for nummer, timestamp in editie:
        if nummer not in nummer_info:
            nummer_info[nummer] = (1, timestamp)
        else:
            count, last_ts = nummer_info[nummer]
            nummer_info[nummer] = (count + 1, max(last_ts, timestamp))

    gesorteerd = sorted(nummer_info.items(), key=lambda item: (-item[1][0], # stemmen aflopend
                                                                item[1][1], # timestamp oplopend
                                                                int(item[0][2]), # release_jaar oplopend oud-nieuw 
                                                                item[0][1], # titel alfabetisch (oplopend)
                                                                item[0][0])) # artiest alfabetisch (oplopend)
    gesorteerde_nummer_list = [nummer for nummer, irrelevant in (gesorteerd)[:100]] # split info into nummer, and irrelevant, but choose only nummer
    return gesorteerde_nummer_list

def maak_stemmenlijst(pad_naar_bestand_met_stemmen: str) -> Stemmenlijst:
    """create a stemmenlijst (list where each item is an element of type Stem)

    Args:
        pad_naar_bestand_met_stemmen (str): path to the input file with votes

    Returns:
        Stemmenlijst: list where each item is an element of type Stem
    """
    with open(pad_naar_bestand_met_stemmen) as fp:
        stemmen_lijst = []
        csv_reader = csv.reader(fp, delimiter=";")
        for item in csv_reader:
            nummer = (item[0], item[1], item[2]) # Nummer = tuple(str, str, int) (artiest, titel, release_jaar)
            naam_van_stemmer = item[3]
            email = item[4]
            timestamp = item[5]
            stem = Stem(nummer, naam_van_stemmer, email, timestamp)
            stemmen_lijst.append(stem)
        return stemmen_lijst


def filter_email(stemmenlijst: Stemmenlijst) -> Stemmenlijst:
    """filter stemmenlijst based on whether an email is valid

    Args:
        stemmenlijst (Stemmenlijst): list where each item is an element of type Stem

    Returns:
        Stemmenlijst: stemmenlijst where each item has a valid email
    """
    pattern = re.compile(r"(?P<local>[a-zA-Z0-9-_.]+)@(?P<domain>((?P<d_part_1>[a-zA-Z0-9-]+)\.)+(?P<d_part_2>[a-zA-Z]+)$)")

    def valid_local(local):
        if local.startswith(".") or local.endswith("."):
            return False
        if ".." in local:
            return False
        return True

    def valid_domain(domain):
        parts = domain.split(".")
        if len(parts) < 2:
            return False
        for part in parts:
            if len(part) < 1:
                return False
            if part.startswith("-") or part.endswith("-"):
                return False
        return True

    def valid_email(email):
        match = pattern.fullmatch(email)
        if not match:
            return False
        local = match.group('local')
        domain = match.group('domain')
        return valid_local(local) and valid_domain(domain)

    geldige_stemmen_lijst = []
    for item in stemmenlijst:
        if valid_email(item.email):
            geldige_stemmen_lijst.append(item)
    return geldige_stemmen_lijst


def filter_laatste_stem(stemmenlijst: Stemmenlijst) -> Stemmenlijst:
    """get list of votes (stemmenlijst) where each email can have at most 1 vote, the most recent vote get's saved

    Args:
        stemmenlijst (Stemmenlijst): list of votes

    Returns:
        Stemmenlijst: list of unique votes
    """
    unieke_emails_stemmen_lijst = []
    for item in stemmenlijst:
        present = False
        for index, item_in in enumerate(unieke_emails_stemmen_lijst):
            if item.email == item_in.email:
                present = True
                if item.timestamp > item_in.timestamp:
                    unieke_emails_stemmen_lijst[index] = item
                    break
        if not present:
            unieke_emails_stemmen_lijst.append(item)

    return unieke_emails_stemmen_lijst

def filter_domein(stemmenlijst: Stemmenlijst, domein: str) -> Stemmenlijst:
    """return stemmenlijst without the items with a specific domain

    Args:
        stemmenlijst (Stemmenlijst): list of votes
        domein (str): domain of items which have to be excluded from the return list

    Returns:
        Stemmenlijst: list of items which don't have the input domain "domein" as their domain
    """
    pattern = re.compile(r"(?P<local>[a-zA-Z0-9-_.]+)@(?P<domain>((?P<d_part_1>[a-zA-Z0-9-]+)\.)+(?P<d_part_2>[a-zA-Z]+)$)")
    zonder_domein_stemmenlijst = []
    for item in stemmenlijst:
        email = pattern.fullmatch(item.email)
        if email and email.group("domain") == domein:
            continue
        else:
            zonder_domein_stemmenlijst.append(item)
    return zonder_domein_stemmenlijst