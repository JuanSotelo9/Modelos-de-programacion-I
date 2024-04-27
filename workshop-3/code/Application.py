from abc import ABC, abstractmethod
from datetime import datetime
import psutil
from UserManager import User, UsersManager
from Catalog import Catalog
from UserController import UserControllerProxy
from AdminController import AdminControllerProxy

class Application(ABC):

    def __init__(self, users_manager: UsersManager, catalog: Catalog) -> None:
        self.controller = None
        self.users_manager = users_manager
        self.catalog = catalog

    @abstractmethod
    def run(self):
        """This method is the main of the application"""

class MainApplication(Application):

    def run(self):
        print("Welcome to the User System!")
        while True:
            print("\n 1. Login \n 2. Register")
            option = int(input("Select a option: "))

            if option == 1:
                user = self.login();
                if user == None:
                    print("Invalid username or password, or that user does not exist.")
                else:
                    print(f"Welcome back, {user.get_username()}!")
                    if user.get_type_user() == "User":
                        self.controller = UserControllerProxy(user, self.catalog)
                        self.controller.events()
                    else:
                        self.controller = AdminControllerProxy(user, self.catalog)
                        self.controller.events()
            elif option == 2:
                self.register();

    def login(self) -> User:
        print("Please log in with your username and password:")
        username = input("Username: ")
        password = input("Password: ")
        return self.users_manager.login(username, password)

    def register(self):
        print("Please provide the following information to register:")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        while True:
            try:
                option = int(input("Select a type user \n 1. User \n 2. Admin\n"))
                if(option == 1):
                    type_user = "User"
                    break;
                elif(option == 2):
                    type_user = "Admin"
                    break;
            except:
                print("Enter a valid option")

        confirm = self.users_manager.register(name, email, username, password, type_user)
        if(confirm):
            print("Registration successful!")
        else:
            print("User already exists")

class Monitoring(Application):
    
    def __init__(self, application) -> None:
        super().__init__()
        self.wrapped = application
        self.monitoring_file = "monitoring.txt"

    def run(self):
        self.__monitor_start()
        memory_before = self.__get_memory_usage()
        self.wrapped.run()
        memory_after = self.__get_memory_usage()
        self.__monitor_end(memory_before, memory_after)

    def __monitor_start(self):
        with open(self.monitoring_file, "a") as file:
            file.write(f"Monitoring started at: {datetime.now()}")

    def __monitor_end(self, memory_before, memory_after):
        with open(self.monitoring_file, "a") as file:
            file.write(f"Memory consumption during execution: {memory_after - memory_before} bytes")
            file.write(f"Monitoring ended at: {datetime.now()}")

    def __get_memory_usage(self):
        process = psutil
        memory_usage = process.memory_info().rss
        return memory_usage
    
userManager = UsersManager()
catalog = Catalog()
app = MainApplication(userManager, catalog)
app.run()