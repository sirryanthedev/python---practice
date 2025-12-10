# (ex. eurovision song contest - Dodona)

def showScores(dictionairy: dict, n = 0):
    data_list = sorted(dictionairy.items(), key=lambda item: (-item[1], item[0]))
    if 0 < n < len(dictionairy):
        return data_list[:n]
    return data_list

def addScores(scoreboard: dict, scores: dict):
    for score in scores.keys():
        if score in scoreboard.keys():
            scoreboard[score] += scores[score]
        else:
            scoreboard[score] = scores[score]

# The Eurovision Song Contest is a yearly competition that is held among the countries that are a member of the European Broadcasting Union (EBU).

# Every participating country sends in a song that is sung live during a television program that is broadcast simultaneously by the EBU in all countries in the Eurovision network. After all songs are performed, a (tele)voting follows after which the winner is announced. The winner of the festival is determined by giving points for every participating country to ten of their favourite songs. Since 1975 this is 1 till 8, then 10 and eventually 12 points for the most popular song. The participating countries are not allowed to vote for themselves.

# The final of the Eurovision Song Contest in 2012 took place in Baku, the capital of Azerbaijan, on 26 May 2012. The festival was won by the Swedish singer Loreen with the song Euphoria. This song got a total of 372 points. Russia and Serbia respectively got second and third place. 

# Assignment
# Write a function addScores, that a country can use to appoint scores to its favourite songs. Two dictionaries should be given to this function as arguments. The first dictionary links the countries to the number of points they have received until now. The second dictionary links the countries to the amount of points they were appointed by another country. The function must update the given dictionary that links each country to the amount of points the country has received with new scores from the second dictionary that was given to the function. In other words, the function must not print a value (or the value None), but update the dictionary that was given as a first argument (dictionaries are after all mutable in Python). The dictionary that is given as a second argument may not be modified by the function.

# Write a function showScores to which a dictionary must be given as an argument. This dictionary links countries to the amount of point they have received so far. The function must print a list of tuples as a result, where every tuple consists of two elements: the name of a country, and the number of points that country has so far. These tuples must be ordered in decreasing number of points. Countries that have an equal score must be ordered alphabetically. To this function a second, optional, integer-argument 
#  can be given. If this is the case, only the first 
#  countries must be printed. The dictionary that is given as an argument of the function may not be modified by the function. 

# Example
# >>> scoreboard = {}

# >>> scores_UK = {'Lithuania': 7, 'Russia': 3, 'Estonia': 4, 'Azerbaijan': 2, 'Sweden': 12, 'Turkey': 1, 'Spain': 8, 'Germany': 6, 'Malta': 5, 'Ireland': 10}
# >>> addScores(scoreboard, scores_UK)
# >>> showScores(scoreboard)
# [('Sweden', 12), ('Ireland', 10), ('Spain', 8), ('Lithuania', 7), ('Germany', 6), ('Malta', 5), ('Estonia', 4), ('Russia', 3), ('Azerbaijan', 2), ('Turkey', 1)]

# >>> scores_HU = {'Albania': 8, 'Russia': 7, 'Iceland': 6, 'Italy': 5, 'Sweden': 12, 'Turkey': 3, 'Spain': 1, 'Germany': 10, 'Serbia': 4, 'Moldova': 2}
# >>> addScores(scoreboard, scores_HU)
# >>> showScores(scoreboard, 3)
# [('Sweden', 24), ('Germany', 16), ('Ireland', 10)]
