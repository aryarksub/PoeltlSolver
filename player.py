# player.py
# 3-25-2022

from constraints import *
import utility as util

class Player:
    def __init__(self, name, team = "", pos = "", height = "",
                 age = "", number = ""):
        self.name = name
        self.team = team
        self.division = util.getDivision(team) if team else ""
        self.conf = util.getConference(self.division) if self.division else ""
        self.positions = pos.split('-') # store G-F as ['G', 'F']
        self.height = height
        self.age = age
        self.number = number
        self.slug = util.cleanString(name)

    def get_slug(self):
        return self.slug

    # Return True if the player matches the given constraints.
    # Otherwise, return False.
    def match(self, constraints: ConstraintSet):
        if not (self.team and self.division and self.conf and self.positions
                and self.height and self.age and self.number):
            return False

        # Team check
        if self.team not in constraints.teams:
            return False

        # Division check
        if self.division not in constraints.divs:
            return False

        # Conference check
        if self.conf not in constraints.confs:
            return False

        # Position check
        for pos in self.positions:
            if pos in constraints.positions:
                break
        else:
            return False

        # Height check
        if (compareHeights(self.height, constraints.minHt) == -1 or
            compareHeights(self.height, constraints.maxHt) == 1):
            return False

        # Age check
        if self.age < constraints.minAge or self.age > constraints.maxAge:
            return False

        # Number check
        if self.number < constraints.minNum or self.number > constraints.maxNum:
            return False

        return True
        

    def __str__(self):
        return self.name + ("(" + self.team + ")" if self.team else "")
