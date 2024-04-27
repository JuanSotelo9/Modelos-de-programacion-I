"""
This file contains a Catalog class and the methods to use
"""

from typing import List
from Vehicles import Vehicle
from Engine import Engine
from Factories import HighEngineFactory, LowEngineFactory


class Catalog:
    
    def __init__(self) -> None:
        self.__vehicles = List[Vehicle]
        self.__engines = List[Engine]
        self.__factory = None
        self.__high_factory = HighEngineFactory()
        self.__low_factory = LowEngineFactory()

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Catalog, cls).__new__(cls)
            cls.instance.__vehicles = []
            cls.instance.__engines = []
        return cls

    def get_vehicles(self):
        """This method show all vehicles of the catalog"""
        return self.__vehicles

    def add_vehicles(
        self, chasis, price, model, year, consumption, type_engine, gamma_engine
    ):
        """This method create a new vehicle in the catalog"""
        for engine in self.__engines:
            if engine.get_cost() == gamma_engine and engine.get_type_() == type_engine:
                self.__vehicles.append(
                    Vehicle(engine, chasis, price, model, year, consumption)
                )
                return True
        if gamma_engine == "High":
            self.__factory = self.__high_factory
        elif gamma_engine == "Low":
            self.__factory = self.__low_factory
        else:
            return False
        if type_engine == "Gas":
            engine = self.__factory.create_gas_engine()
        elif type_engine == "Electric":
            engine = self.__factory.create_electric_engine()
        else:
            return False

        self.__engines.append(engine)
        self.__vehicles.append(Vehicle(engine, chasis, price, model, year, consumption))

    def get_by_maximum_speed(self, maximum_speed):
        """This method search vehicles for maximum_spped"""
        return [
            vehicle
            for vehicle in self.__vehicles
            if maximum_speed == vehicle.get_maximum_speed()
        ]

    def get_by_type_combustion(self, type_combustion):
        """This method search vehicles for type_combustion"""
        return [
            vehicle
            for vehicle in self.__vehicles
            if type_combustion == vehicle.get_engine().get_type_()
        ]

    def get_by_range_years(self, min_year, max_year):
        """This method search vehicles for a range of year"""
        return [
            vehicle
            for vehicle in self.__vehicles
            if min_year <= vehicle.get_year() <= max_year
        ]
