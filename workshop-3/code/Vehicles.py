"""
This file has a set of classes related to vehicles,
including of the all subtypes of vehicles.

"""
from Engine import Engine
class Vehicle:
    """This class represents an abstraction of a vehicle inside the catalog business model."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        id_vehicle: str,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
    ):
        self.__id = id_vehicle
        self.__engine = engine
        self.__chassis = chassis
        self.__price = price
        self.__model = model
        self.__year = year

    def get_id(self):
        return self.__id
    
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
    
    def __str__(self):
        return f"Vehicle: {self.__model} - {self.__year} - {self.__price} - \
            {self.__engine} - {self.__chassis}"


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
        transmission: str,
        trade: str,
        combustible_type: str,
    ):
        super().__init__(engine, chassis, price, model, year)
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type


class Truck(Vehicle):
    """This class is a concrete implemtantion of a truck"""

    def __init__(self, engine: Engine, chassis: str, price: float, model: str, year: int):
        super().__init__(engine, chassis, price, model, year)
        self.consumption = self.calculate_gas_consupmtion()

    def calculate_gas_consupmtion(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.__engine.get_power())
            + (0.2 * self.__engine.get_weight())
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
        length: float,
        weight: float,
        trade: str,
    ):
        super().__init__(engine, chassis, price, model, year)
        self.length = length
        self.weight = weight
        self.trade = trade