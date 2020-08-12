# coding=utf-8
from utils.errors import validateNonZero


class Airplane(object):

    def __init__(self, initX, initY, consumption, initial_fuel_level):
        """
        Initialise Airplane with positive numbers.
        Error raised for zero and negative numbers.
        """
        self.consumption = consumption
        self.fuel_level = initial_fuel_level
        self.position = (initX, initY)

    @property
    def consumption(self):
        return self._consumption

    @consumption.setter
    def consumption(self, value):
        self._consumption = validateNonZero('consumption', value)

    @property
    def fuel_level(self):
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, value):
        self._fuel_level = validateNonZero('fuel_level', value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = (validateNonZero('initX',value[0]),validateNonZero('initY', value[1]))

    def refuel(self, fuel):
        """
        Refuel plane by incrementing fuel to fuel_level.
        Error raised for zero and negative number.
        """
        self.fuel_level += fuel

    def goto(self, X, Y):
        """
        Moves plane's location to new position X and Y if there is enough fuel.
        Returns False if there is not enough fuel to fly there, else flies there and returns True.
        Error raised for zero and negative numbers.
        Note: math.sqrt could have been used instead of ** (1/2) although possibly slower.
        """
        if not(self.position[0] == X and self.position[1] == Y):
            distance = (((X - self.position[0]) ^ 2) + ((Y - self.position[1]) ^ 2)) ** (1 / 2)
            potential_fuel_consumption = distance * self.consumption
            if self.fuel_level >= potential_fuel_consumption:
                self.fuel_level -= potential_fuel_consumption
                self._position = (X, Y)
                return True
            else:
                return False
        else:
            return True