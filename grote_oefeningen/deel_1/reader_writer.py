from tijdloze100_types import *
from os import getcwd, listdir
from os.path import isdir, isfile, join
import re, csv

def lees_tijdloze100(root_folder: str) -> Edities:
    """extract info from root map which contains folders where each folder is named after a year (e.g. 1987), each of those folders contains 100 subfolders named nummer_{x} where x is a number from 1 through 100 and each of those subfolders contains 3 files from which we extract the info

    Args:
        root_folder (str): folder which contains folders named after years with their subfolders and info (e.g. tijdloze)

    Raises:
        FileNotFoundError: if artiest.txt or titel.txt or release_jaar.txt not present, raise error

    Returns:
        Edities: dictionairy[key: year of the folder, value: tuple with info(artiest, titel, release_jaar)]
    """
    folder_list_1 = listdir(root_folder)
    edities = {}
    for item_1 in folder_list_1:
        full_path_1 = join(root_folder, item_1) # year-folders (e.g. 1987)
        editie = [None for _ in range(100)] # map of all 100 nummers per year-folder, fill it with 100 None's first, to make it approachable via index
        if isdir(full_path_1):
            for item_2 in listdir(full_path_1): # nummer-folders
                full_path_2 = join(full_path_1, item_2)
                pos = re.search(r"nummer_(\d+)", item_2)
                if isdir(full_path_2): # look inside nummer-folders
                    artist = ""
                    title = ""
                    release_year = 0
                    for item_3 in listdir(full_path_2):
                        if "artiest.txt" in listdir(full_path_2) and "titel.txt" in listdir(full_path_2) and "release_jaar.txt" in listdir(full_path_2):
                            if item_3 == "artiest.txt":
                                with open(join(full_path_2, item_3)) as fp:
                                    buffer = fp.read()
                                    artist = buffer
                            elif item_3 == "titel.txt":
                                with open(join(full_path_2, item_3)) as fp:
                                    buffer = fp.read()
                                    title = buffer
                            elif item_3 == "release_jaar.txt":
                                with open(join(full_path_2, item_3)) as fp:
                                    buffer = fp.read()
                                    release_year = buffer
                        else:
                            raise FileNotFoundError("A file of type .txt is missing...")
                    if artist and title and release_year:
                        nummer = (artist, title, release_year)
                        if editie[int(pos.group(1)) - 1] is None:
                            editie[int(pos.group(1)) - 1] = nummer
            edities[int(item_1)] = editie
    return edities

def schrijf_tijdloze100(edities: Edities, csv_out: str) -> None:
    """write info from edities to a csv file

    Args:
        edities (Edities): dictionairy[key: year of the folder, value: tuple with info(artiest, titel, release_jaar)]
        csv_out (str): output file
    """
    with open(csv_out, "a", newline="", encoding = "utf-8") as fp:
        writer = csv.writer(fp, delimiter=";")
        for year in edities.keys():
            for index, value in enumerate(edities[year]):
                to_add = (year, index + 1) + value # concatenate tuples to get this format e.g. 1987;1; Deep Purple ; Child in Time ;1970
                writer.writerow(to_add) # write each to_add tuple to csv_out