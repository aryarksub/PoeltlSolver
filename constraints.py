# constraints.py
# 3-25-2022

from collections import namedtuple

ConstraintSet = namedtuple("ConstraintSet", ["teams", "confs", "divs",
                                             "positions", "minHt", "maxHt",
                                             "minAge", "maxAge", "minNum",
                                             "maxNum"])

Guess = namedtuple("Guess", ["name", "teamColor", "confColor", "divColor",
                                "posColor", "htColor", "ageColor", "numColor"])

def updateConstraints(cSet, guess):
    # Get team, conf, div, pos, ht, age, num of player given name in guess
    pass
