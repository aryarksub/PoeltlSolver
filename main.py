# main.py
# 4-10-2022

import csv
import utility as util
from player import Player

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
    pass


def run():
    playerDict = createPlayerDict()
    for x in playerDict:
        print(x, playerDict[x])



if __name__ == '__main__':
    run()