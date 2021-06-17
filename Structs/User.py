class User:
    def __init__(self, login, id_user):
        self.__login = login
        self.__id = id_user

    def getLogin(self):
        return self.__login

    def getId(self):
        return self.__id
