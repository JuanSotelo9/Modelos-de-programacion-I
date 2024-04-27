class User:

    def __init__(self, name: str, email: str, username: str, password: str, type_user: str) -> None:
        self.__name = name
        self.__email = email
        self.__username = username
        self.__password = password
        self.__type_user = type_user

    def get_name(self) -> str:
        return self.__name
    
    def get_email(self) -> str:
        return self.__email
    
    def get_username(self) -> str:
        return self.__username
    
    def get_password(self) -> str:
        return self.__password
    
    def get_type_user(self) -> str:
        return self.__type_user
    

class UsersManager:

    def __init__(self) -> None:
        self.__users = []

    def register(self, name, email, username, password, type_user) -> bool:
        for user in self.__users:
            if(username == user.get_username() or email == user.get_email()):
                return False

        self.__users.append(User(name, email, username, password, type_user))
        return True

    def login(self, username, password) -> User:
        user = self.find_user(username)
        if(user.get_password() == password):
            return user
        else:
            return None

    def find_user(self, username) -> User:
        for user in self.__users:
            if(user.get_username() == username):
                return user

    def get_users(self):
        return self.__users