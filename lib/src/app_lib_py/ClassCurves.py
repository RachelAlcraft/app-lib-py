"""
Class for different kinds of curves with an abstract base class Curve
"""

from abc import ABC, abstractmethod
import math


class Curve(ABC):
    @abstractmethod
    def get_ys(self, xs):
        pass


class Quadratic(Curve):
    """Class for curves of the quadratic form y = ax^2 + bx + c"""

    def __init__(self, a, b, c):
        """Initialise the quadratic with values for a,b and c"""
        self.a = a
        self.b = b
        self.c = c

    def get_ys(self, xs):
        """Request y points for the given x series"""
        ys = []
        for x in xs:
            y = self.a * math.pow(x, 2)
            y += self.b * x
            y += self.c
            ys.append(y)
        return ys


class Exponential(Curve):
    """Class for curves of the exponential form y = ae^bx + c"""

    def __init__(self, a, b, c):
        """Initialise the exponential with values for a,b,c for y = ae^bx + c"""
        self.a = a
        self.b = b
        self.c = c

    def get_ys(self, xs):
        ys = []
        for x in xs:
            y = self.a * math.exp(x * self.b)
            y += self.c
            ys.append(y)
        return ys
