from enum import Enum
from os import X_OK
from telnetlib import X3PAD

from attr import define
from numpy import kaiser

class Rank(Enum):
    II    = 2
    III   = 3
    IV    = 4
    V     = 5
    VI    = 6
    VII   = 7
    VIII  = 8
    IX    = 9
    X     = 10
    J     = 11
    Q     = 12
    K     = 13
    A     = 14