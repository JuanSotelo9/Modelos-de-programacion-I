"""
This file contains a Catalog class and the methods to use
"""

from Vehicles import Vehicle
from Factories import EngineFlyweightFactory

class Catalog:
    
    def __init__(self) -> None:
        self.__vehicles = []

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Catalog, cls).__new__(cls)
            cls.instance.__vehicles = []
        return cls.instance

    def get_vehicles(self):
        """This method show all vehicles of the catalog"""
        return self.__vehicles

    def add_vehicles(
        self, id_vehicle, chasis, price, model, year, type_engine, gamma_engine
    ):
        """This method create a new vehicle in the catalog"""
        engine = EngineFlyweightFactory.get_engine(gamma_engine, type_engine)
        vehicle = Vehicle(id_vehicle, engine, chasis, price, model, year)
        self.__vehicles.append(vehicle)

    def get_by_maximum_speed(self, maximum_speed):
        """This method search vehicles for maximum_spped"""
        return [
            vehicle
            for vehicle in self.__vehicles
            if maximum_speed == vehicle.get_engine().get_maximum_speed()
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
