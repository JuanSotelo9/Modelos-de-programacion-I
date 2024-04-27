from abc import ABC, abstractmethod
from datetime import datetime
from Controller import Controller

class AdminController(Controller):
    
    def events(self):
        while True:
            print("\nVehicle Management System")
            print("1. Create Vehicle")
            print("2. Update Vehicle")
            print("3. Delete Vehicle")
            print("4. Exit")
            option = int(input())
            if option == 1:
                self.create_vehicle()
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

    def create_vehicle(self):
        print("Enter Vehicle Information:")
        id_vehicle = input("ID Vehicle: ")
        chasis = input("Chasis: ")
        price = float(input("Price: "))
        model = input("Model: ")
        year = int(input("Year: "))
        type_engine = input("Type of Engine: ")
        gamma_engine = input("Gamma Engine: ")
        self.catalog.add_vehicles(id_vehicle, chasis, price, model, year, type_engine, gamma_engine)

    def delete_vehicle(self):
        id_vehicle = input("Enter id vehicle: ")
        return f"delete the vehicle {id_vehicle}"
    
    def update_vehicle(self):
        id_vehicle = input("Enter id vehicle")
        new_info = input("Enter the new info")
        attribute = input("Enter the attribute")
        return f"update the vehicle {id_vehicle}, new infor {new_info}, attribute {attribute}"
    
class AdminControllerProxy(Controller):

    def __init__(self, user, catalog):
        super().__init__(user, catalog)
        self.real_service = AdminController(user, catalog)
        self.log_file = "logging.txt"

    def events(self):
        while True:
            print("\nVehicle Management System")
            print("1. Create Vehicle")
            print("2. Update Vehicle")
            print("3. Delete Vehicle")
            print("4. Exit")
            option = int(input())
            if option == 1:
                self.create_vehicle()
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

    def logging(self, username, action):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()}.Admin {username} {action}")

    def create_vehicle(self):
        print("Enter Vehicle Information:")
        id_vehicle = input("ID Vehicle: ")
        chasis = input("Chasis: ")
        price = float(input("Price: "))
        model = input("Model: ")
        year = int(input("Year: "))
        type_engine = input("Type of Engine: ")
        gamma_engine = input("Gamma Engine: ")
        self.logging(self.user.get_username(), "create a new vehicle")
        
        self.real_service.create_vehicle(id_vehicle, chasis, price, model, year, type_engine, gamma_engine)

    def delete_vehicle(self):
        id_vehicle = input("Enter id vehicle: ")
        self.logging(self.user.get_username(), "delete a vehicle")

        return self.real_service.delete_vehicle(id_vehicle)
    
    def update_vehicle(self):
        id_vehicle = input("Enter id vehicle")
        new_info = input("Enter the new info")
        attribute = input("Enter the attribute")
        self.logging(self.user.get_username(), "update a vehicle")
        return self.real_service.update_vehicle(id_vehicle, new_info, attribute)
    