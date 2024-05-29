"""
This module has a definition of both an interface and a concrete definition for Catalogs.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from typing import List

from .catalog_interface import Catalog
from ..vehicles_subsystem import Vehicle, VehiclesFacade
from .vehicle_memento import VehicleHistory, VehicleMemento
from .cache import Cache

class CatalogConcrete(Catalog):
    """
    This is a concrete implementation of the Catalog interface.

    Methods:
        get_all_vehicles -> list: This method returns a list of all vehicles in the catalog.
        get_by_speed -> List[Vehicle]: This method returns a list of vehicles that have a speed
                                       between min_speed and max_speed.
        get_by_price -> List[Vehicle]: This method returns a list of vehicles that have a price
                                       between min_price and max_price.
        add_vehicle: This method adds a vehicle to the catalog.
        remove_vehicle: This method removes a vehicle from the catalog.
    """

    def __init__(self):
        self.__vehicles = []
        self.__vehicles_facade = VehiclesFacade()
        self.__history = VehicleHistory()
        self.__cache = Cache()

    def get_all_vehicles(self) -> List[Vehicle]:
        return self.__vehicles

    def get_by_speed(self, min_speed: int, max_speed: int) -> List[Vehicle]:

        result = self.__cache.get_search_result(f'speed {min_speed}-{max_speed}')
        if(result == None):
            result = [
                vehicle
                for vehicle in self.__vehicles
                if vehicle.is_in_speed(min_speed, max_speed)
            ]
            self.__cache.add_search_result(f'speed {min_speed}-{max_speed}', result)
        
        return result

    def get_by_price(self, min_price: int, max_price: int) -> List[Vehicle]:
        result = self.__cache.get_search_result(f'price {min_price}-{max_price}')
        if(result == None):

            result = [
                vehicle
                for vehicle in self.__vehicles
                if vehicle.is_in_price(min_price, max_price)
            ]
            self.__cache.add_search_result(f'price {min_price}-{max_price}', result)

        return result

    def add_vehicle(self, vehicle_type: str):
        self.__vehicles.append(self.__vehicles_facade.create_vehicle(vehicle_type))
        self.__cache.clear_cache()

    def remove_vehicle(self, vehicle: Vehicle):
        self.__vehicles.remove(vehicle)
        self.__history.save_state(VehicleMemento(vehicle))
        self.__cache.clear_cache()

    def recover_last_delete_vehicle(self):
        memento = self.__history.get_last_saved()
        if memento:
            self.__vehicles.append(memento.get_saved_vehicle())
        self.__cache.clear_cache()

    def get_last_five(self):
        if len(self.__vehicles) <= 5 :
            return self.__vehicles
        else:
            return self.__vehicles[-5:]