"""
This file has a set of classes related to vehicles,
including of the all subtypes of vehicles.

"""

from Engine import Engine


# pylint: disable=too-few-public-methods
class Vehicle:
    """This class represents an abstraction of a vehicle inside the catalog business model."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
    ):
        self.__engine = engine
        self.__chassis = chassis
        self.__price = price
        self.__model = model
        self.__year = year
        self.__consumption = consumption

    def get_engine(self):
        return self.__engine
    
    def get_chasis(self):
        return self.__chassis
    
    def get_price(self):
        return self.__price
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_consumption(self):
        return self.__consumption
    
    def __str__(self):
        return f"Vehicle: {self.__model} - {self.__year} - {self.__price} - \
            {self.__consumption} - {self.__engine} - {self.__chassis}"


class Helicopter(Vehicle):
    """This class is a concrete implementation of an helicopter"""


class Scooter(Vehicle):
    """This class is a concrete implementation of a scoorter"""


class Motorcycle(Vehicle):
    """This class is a concrete implementation of a motorcycle"""


class Car(Vehicle):
    """This class is a concrete implementation of a car"""

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        transmission: str,
        trade: str,
        combustible_type: str,
    ):
        super().__init__(engine, chassis, price, model, year, consumption)
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type


class Truck(Vehicle):
    """This class is a concrete implemtantion of a truck"""

    def calculate_gas_consupmtion(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.__engine.power)
            + (0.2 * self.__engine.weight)
            + (0.3 if self.__chassis == "A" else 0.5)
        )
        return consumption


class Yacht(Vehicle):
    """This class is a concrete implementation of a yatch"""

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        length: float,
        weight: float,
        trade: str,
    ):
        super().__init__(engine, chassis, price, model, year, consumption)
        self.length = length
        self.weight = weight
        self.trade = trade