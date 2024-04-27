from abc import ABC, abstractmethod
from datetime import datetime
from Controller import Controller

class UserController(Controller):

    def events(self):
        while True:
            print("\nMenu Options:")
            print("1. View all vehicles")
            print("2. Search by maximum speed")
            print("3. Search by combustion type")
            print("4. Search by year range")
            print("5. Exit")
            option = int(input())
            if option == 1:
                self.show_results(self.viewVehicles())
            elif option == 2:
                maximum_speed = int(input("Enter a maximum speed: "))
                self.show_results(self.search_by_maximum_speed(maximum_speed))
            elif option == 3:
                type_combustion = input("Enter a combustion type: ")
                self.show_results(self.search_by_type_combustion(type_combustion))
            elif option == 4:
                min_year = int(input("Enter a min year: "))
                max_year = int(input("Enter a max year: "))
                self.show_results(self.search_by_range_year(min_year, max_year))
            elif option == 5:
                break;

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
    
    def show_results(self, results):
        if(len(results) == 0):
            print("There are not results of the search")
        else:
            for result in results:
                print(result)
    
class UserControllerProxy(Controller):

    def __init__(self, user, catalog) -> None:
        super().__init__(user, catalog)
        self.real_service = UserController(user, catalog)
        self.cache = []
        self.log_file = "logging.txt"

    def events(self):
        while True:
            print("\nMenu Options:")
            print("1. View all vehicles")
            print("2. Search by maximum speed")
            print("3. Search by combustion type")
            print("4. Search by year range")
            print("5. Exit")
            option = int(input())
            if option == 1:
                self.show_results(self.viewVehicles())
            elif option == 2:
                maximum_speed = int(input("Enter a maximum speed: "))
                self.show_results(self.search_by_maximum_speed(maximum_speed))
            elif option == 3:
                type_combustion = input("Enter a combustion type: ")
                self.show_results(self.search_by_type_combustion(type_combustion))
            elif option == 4:
                min_year = int(input("Enter a min year: "))
                max_year = int(input("Enter a max year: "))
                self.show_results(self.search_by_range_year(min_year, max_year))
            elif option == 5:
                break;
    
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
    
    def show_results(self, results):
        if(len(results) == 0):
            print("There are not results of the search")
        else:
            for result in results:
                print(result)
