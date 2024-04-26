"""
    This file has some classes related to engines, inclusing types
"""

class Engine:
    """This class represents an abstraction of an engine for any vehicle."""

    def __init__(
        self,
        torque: int,
        maximum_speed: int,
        dimenssions: str,
        power: int,
        stability: str,
        weight: float,
        cost: str,
        type_: str
    ):
        self.__torque = torque
        self.__maximum_speed = maximum_speed
        self.__dimenssions = dimenssions
        self.__power = power
        self.__stability = stability
        self.__weight = weight
        self.__cost = cost
        self.__type_ = type_

    def get_torque(self):
        return self.__torque
    
    def get_maximum_speed(self):
        return self.__maximum_speed
    
    def get_dimenssions(self):
        return self.__dimenssions
    
    def get_power(self):
        return self.__power
    
    def get_stability(self):
        return self.__stability
    
    def get_weight(self):
        return self.__weight
    
    def get_cost(self):
        return self.__cost
    
    def get_type_(self):
        return self.__type_
    
class GasEngine(Engine):
    """This class represents the behavior of a gas engine"""

class ElectricEngine(Engine):
    """This class represents the behavior of a electric engine"""