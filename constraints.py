# constraints.py
# 3-25-2022

from collections import namedtuple

ConstraintSet = namedtuple("ConstraintSet", ["teams", "confs", "divs",
                                             "positions", "minHt", "maxHt",
                                             "minAge", "maxAge", "minNum",
                                             "maxNum"])
