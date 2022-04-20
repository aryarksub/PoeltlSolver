# main.py
# 4-10-2022

import csv

from pandas import json_normalize
import utility as util
from player import Player
import json

'''
Create player dictionary that maps cleaned player names to Player objects
using data from Basketball Reference. The dictionary values are
semi-initialized Player objects that only contain player names, ages,
teams, and slugs (cleaned names).
'''
def createPlayerDict():
    playerDict = dict()
    with open("bball_ref.csv", 'r', encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            playerAndSlug, age, team = row[1], row[3], row[4]
            # team = 'TOT' denotes a player who has played for more than
            #   one team in a season. The most recent team will appear
            #   later and we can create a Player instance with that data row
            if team == 'TOT':
                continue
            playerName = playerAndSlug.split('\\')[0]
            cleanString = util.cleanString(playerName)
            player = Player(playerName, team=team, age=age, slug=cleanString)
            playerDict[cleanString] = player
    return playerDict

'''
Fill the given dictionary that maps cleaned player names to Player objects
with the necessary missing attributes (position, height, and number) using
data rows from the NBA.com data file.
'''
def fillPlayerDict(pDict):
    with open("nba_players.txt") as jsonFile:
        jsonObject = json.load(jsonFile)
    resultSets = jsonObject["resultSets"]
    players = resultSets[0]["rowSet"]
    for playerRow in players:
        lname, fname, num, pos, ht, to_year = playerRow[1], playerRow[2], playerRow[10], playerRow[11], playerRow[12], playerRow[-1]
        slug = util.cleanString(fname + lname)
        # only consider players who have played through the past season and
        #   also appear in the player dict created using bball reference data
        if (to_year == "2020" or to_year == "2021") and slug in pDict:
            pDict[slug].set_attribute("positions", pos.split('-'))
            pDict[slug].set_attribute("height", ht)
            pDict[slug].set_attribute("number", num)
        elif (to_year == "2020" or to_year == "2021") and slug not in pDict:
            pass#print(slug)
    for p in pDict:
        for a in ['name', 'team', 'division', 'conf', 'positions', 'height', 'age', 'number', 'slug']:
            if pDict[p].get_attribute(a) == "":
                print(p, pDict[p], a)
    



def run():
    playerDict = createPlayerDict()
    fillPlayerDict(playerDict)



if __name__ == '__main__':
    run()