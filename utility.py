# utility.py
# 3-25-2022

import unidecode

# POTENTIAL FIXES: Brooklyn Nets (BRK -> BKN), Charlotte Hornets (CHO -> CHA)
confToDivs = {"East" : {"Atl.", "Cen.", "SE"}, 
                "West" : {"NW", "Pac.", "SW"}}
divToTeams = {"Atl." : {"BOS", "BRK", "NYK", "PHI", "TOR"}, 
                "Cen." : {"CHI", "CLE", "DET", "IND", "MIL"},
                "SE" : {"ATL", "CHO", "MIA", "ORL", "WAS"},
                "NW" : {"DEN", "MIN", "OKC", "POR", "UTA"},
                "Pac." : {"GSW", "LAC", "LAL", "PHO", "SAC"},
                "SW" : {"DAL", "HOU", "MEM", "NOP", "SAS"}}

# Given a team's abbreviation, return its division.
def getDivision(team: str) -> str:
    for div in divToTeams:
        if team in divToTeams[div]:
            return div
    raise ValueError("Invalid team")

# Given a division, return the respective conference.
def getConference(div: str) -> str:
    for conf in confToDivs:
        if div in confToDivs[conf]:
            return conf
    raise ValueError("Invalid division")

# Return s in all lowercase and with only letters.
def cleanString(s: str) -> str:
    no_accents = unidecode.unidecode(s)
    no_suffix = no_accents
    suffixes = ['Jr.', 'Sr.', 'III', 'II']
    for suf in suffixes:
        no_suffix = no_suffix.replace(suf, '')
    res = ''
    for x in no_suffix.lower():
        if ord('a') <= ord(x) <= ord('z'):
            res += x
    return res

# Return -1 if x < y, 0 if x == y, 1 if x > y.
# x and y are strings that represent heights
#   Format: feet'inches"
def compareHeights(x: str, y: str) -> int:
    tokens1 = [int(a.replace('\"', '')) for a in x.split('\'')]
    tokens2 = [int(a.replace('\"', '')) for a in y.split('\'')]
    assert len(tokens1) == len(tokens2) == 2
    if tokens1 < tokens2:
        return -1
    elif tokens1 > tokens2:
        return 1
    return 0
