from abc import ABC, abstractmethod
from datetime import datetime
from vehiclesManager.Catalog import Catalog

class AdminController(ABC):
    """This class represent the controller interface for the user"""

    @abstractmethod
    def create_vehicle(self, chasis, price, model, year, consumption, type_engine, gamma_engine):
        """This method shows all vehicles from the catalog"""

    @abstractmethod
    def delete_vehicle(self, pos):
        """This method shows the result of the search by maximum speed"""

    @abstractmethod
    def update_vehicle(self, pos, new_info, attr):
        """This method shows the result of the search by type cpmbustion"""

class RealAdminController(AdminController):

    def __init__(self, user):
        self.user = user
        self.catalog = Catalog()
    
    def create_vehicle(self, chasis, price, model, year, consumption, type_engine, gamma_engine):
        self.catalog.add_vehicles(chasis, price, model, year, consumption, type_engine, gamma_engine)

    def delete_vehicle(self, pos):
        return f"delete the vehicle {pos}"
    
    def update_vehicle(self, pos, new_info, attr):
        return f"update the vehicle {pos}"
    
class AdminControllerProxy(AdminController):

    def __init__(self, user):
        self.user = user
        self.real_service = RealAdminController(user)
        self.log_file = "logging.txt"

    def logging(self, username, action):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()}.Admin {username} {action}")

    def create_vehicle(self, chasis, price, model, year, consumption, type_engine, gamma_engine):
        self.logging(self.user.get_username(), "create a new vehicle")
        self.real_service.create_vehicle(chasis, price, model, year, consumption, type_engine, gamma_engine)

    def delete_vehicle(self, pos):
        self.logging(self.user.get_username(), "delete a vehicle")
        return self.real_service.delete_vehicle(pos)
    
    def update_vehicle(self, pos, new_info, attr):
        self.logging(self.user.get_username(), "update a vehicle")
        return self.real_service.update_vehicle(pos, new_info, attr)
    