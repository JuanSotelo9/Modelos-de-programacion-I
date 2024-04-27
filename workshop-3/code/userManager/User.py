
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