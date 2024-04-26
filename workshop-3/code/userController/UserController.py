from abc import ABC, abstractmethod
from datetime import datetime
from vehiclesManager.Catalog import Catalog

class UserController(ABC):
    """This class represent the controller interface for the user"""

    @abstractmethod
    def viewVehicles(self):
        """This method shows all vehicles from the catalog"""

    @abstractmethod
    def search_by_maximum_speed(self, maximum_speed):
        """This method shows the result of the search by maximum speed"""

    @abstractmethod
    def search_by_type_combustion(self, type_combustion):
        """This method shows the result of the search by type cpmbustion"""

    @abstractmethod
    def search_by_range_year(self, min_year, max_year):
        """This method shows the result of the search by a rango of year"""

class RealUserController(UserController):

    def __init__(self, user):
        self.user = user
        self.catalog = Catalog()

    def viewVehicles(self):
        return self.catalog.get_vehicles()

    def search_by_maximum_speed(self, maximum_speed):
        """This method shows the result of the search by maximum speed"""
        return self.catalog.get_by_maximum_speed(maximum_speed)
    def search_by_type_combustion(self, type_combustion):
        """This method shows the result of the search by type cpmbustion"""
        return self.catalog.get_by_type_combustion(type_combustion)
    def search_by_range_year(self, min_year, max_year):
        """This method shows the result of the search by a rango of year"""
        return self.catalog.get_by_range_years(min_year, max_year)
    
class UserControllerProxy(UserController):

    def __init__(self, user) -> None:
        self.user = user
        self.real_service = RealUserController(user)
        self.cache = []
        self.log_file = "logging.txt"

    def add_to_cache(self,consult, result, params=[]):
        if len(self.cache) == 5:
            self.cache.pop()
        self.cache.append({"consult" : consult, "params" : params, "result" : result})

    def retrieve_from_cache(self, consult, params):
        for data in self.cache:
            if consult == data["consult"] and params == data["params"]:
                return data["result"]    
        return None
    def logging(self, username, action):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()}.User {username} {action}")

    def viewVehicles(self):
        """This method shows all vehicles from the catalog"""
        self.logging(self.user.get_username(), "viewed all vehicles")
        result = self.retrieve_from_cache("viewVehicles", [])
        if result == None:
            result = self.real_service.viewVehicles()
            self.add_to_cache("viewVehicles", result)
            return result
        else:
            return result
    def search_by_maximum_speed(self, maximum_speed):
        """This method shows the result of the search by maximum speed"""
        self.logging(self.user.get_username(), f"searched by maximum speed {maximum_speed}")
        result = self.retrieve_from_cache("maximum_speed", [maximum_speed])
        if result == None:
            result = self.real_service.search_by_maximum_speed(maximum_speed)
            self.add_to_cache("maximum_speed", result, [maximum_speed])
            return result
        else:
            return result
    def search_by_type_combustion(self, type_combustion):
        """This method shows the result of the search by type cpmbustion"""
        self.logging(self.user.get_username(), f"searched by type combustion {type_combustion}")
        result = self.retrieve_from_cache("type_combustion", [type_combustion])
        if result == None:
            result = self.real_service.search_by_type_combustion(type_combustion)
            self.add_to_cache("type_combustion", result, [type_combustion])
            return result
        else:
            return result
    def search_by_range_year(self, min_year, max_year):
        """This method shows the result of the search by a rango of year"""
        self.logging(self.user.get_username(), f"searched by year range ({min_year}-{max_year})")
        result = self.retrieve_from_cache("range_year", [min_year, max_year])
        if result == None:
            result = self.real_service.search_by_range_year(min_year, max_year)
            self.add_to_cache("range_year", result, [min_year, max_year])
            return result
        else:
            return result
    
