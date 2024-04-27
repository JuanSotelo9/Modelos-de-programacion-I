from UserManager import User
from Catalog import Catalog

class Controller:

    def __init__(self, user: User, catalog: Catalog) -> None:
        self.user = user
        self.catalog = catalog

    def events(self):
        pass