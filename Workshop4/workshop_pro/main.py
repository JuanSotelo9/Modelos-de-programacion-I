"""
This is the main file of the project. It is the entry point of the application.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from .core_subsystem import FinalCatalog, Authentication, User, Newsletter


CATALOG = FinalCatalog()
NEWSLETTER = Newsletter()
MENU_OPTIONS = """
0. Log in the system
1. Subscribe to Newsletter
2. Unsubscribe to Newsletter
3. Notify subscribers
4. Add a new vehicle
5. Remove a vehicle
6. Search all vehicles
7. Search vehicles by speed
8. Search vehicles by price
9. Exit
"""


def login():
    """This function allows the user to log in the system."""
    username = input("Username: ")
    password = input("Password: ")

    auth = Authentication(username, password)

    if auth.authenticate():
        return auth.userdata()
    return None


def main():
    """This if the main file of the project."""
    user = None

    print("Welcome to the Vehicle Catalog System")
    print(MENU_OPTIONS)

    while True:
        option = input("Please select an option: ")

        if option == "0":
            print("====== Logging in the system ======")
            user = login()
        elif option == "1":
            print("====== Subscribe to Newsletter")
            NEWSLETTER.subscribe(user)
        elif option == "2":
            print("====== Unsubscribe to Newsletter")
            NEWSLETTER.unsubscribe(user)
        elif option == "3":
            print("====== Sending notify to subscribers")
            if(user.is_grant("notify")):
                NEWSLETTER.notify_subscribers(CATALOG.get_last_five())
        elif option == "4":
            print("====== Adding a new vehicle ======")
            if user.is_grant("add_vehicle"):
                CATALOG.add_vehicle(user.get_username())
        elif option == "5":
            print("====== Removing a vehicle ======")
            if user.is_grant("remove_vehicle"):
                CATALOG.remove_vehicle(user.get_username())
        elif option == "6":
            print("====== Searching all vehicles ======")
            if user.is_grant("search_vehicle"):
                CATALOG.get_all_vehicles(user.get_username())
        elif option == "7":
            print("====== Searching vehicles by speed ======")
            if user.is_grant("search_vehicle"):
                CATALOG.get_vehicles_by_speed(user.get_username())
        elif option == "8":
            print("====== Searching vehicles by price ======")
            if user.is_grant("search_vehicle"):
                CATALOG.get_vehicles_by_price(user.get_username())
        elif option == "9":
            print("====== Exiting the system ======")
            break
        else:
            print("Invalid option. Please select a valid option.")

        print("\n" + MENU_OPTIONS + "\n\n")

    print("Thank you for using the Vehicle Catalog System.")


if __name__ == "__main__":
    main()
