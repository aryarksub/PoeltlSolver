# utility.py
# 3-25-2022

import unicodedata

# FIX: map div name to list of teams in global dict (FIXED)
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

    # if team in ["BOS", "BRK", "NYK", "PHI", "TOR"]:
    #     return "Atl."
    # if team in ["CHI", "CLE", "DET", "IND", "MIL"]:
    #     return "Cen."
    # if team in ["ATL", "CHO", "MIA", "ORL", "WAS"]:
    #     return "SE"
    # if team in ["DEN", "MIN", "OKC", "POR", "UTA"]:
    #     return "NW"
    # if team in ["GSW", "LAC", "LAL", "PHO", "SAC"]:
    #     return "Pac."
    # if team in ["DAL", "HOU", "MEM", "NOP", "SAS"]:
    #     return "SW"
    raise ValueError("Invalid team")

# Given a division, return the respective conference.
def getConference(div: str) -> str:
    for conf in confToDivs:
        if div in confToDivs[conf]:
            return conf
    # if div in ["Atl.", "Cen.", "SE"]:
    #     return "East"
    # if div in ["NW", "Pac.", "SW"]:
    #     return "West"
    raise ValueError("Invalid division")

# Return s in all lowercase and with only letters.
def cleanString(s: str) -> str:
    res = ''
    for x in s.lower():
        if ord('a') <= ord(x) <= ord('z'):
            res += x
    # Normalize unicode string
    nfkd_form = unicodedata.normalize('NFKD', res)
    # Encode into ASCII (remove accents)
    encoded = nfkd_form.encode('ascii', 'ignore')
    # Return string without accents
    return str(encoded.decode('utf-8'))

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
