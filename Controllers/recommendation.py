import json

from pprint import pprint

from Controllers.connection import Connection
from .person_correlation import person_correlation

class Recommendation:
    def __init__(self):
        self.data_base_connection = Connection()
        self.users_ratings = self.data_base_connection.get_json()
        self.users_ratings = json.loads(self.users_ratings)
    
    def select_kneighbors_for(self, user, k=5):
        """
        This method select neighbors more close of a user using
        person correlation.
        param user str: user name to find neighbors
        param k int: number of neighbors to find, defaul is 5
        """
        distances = []
        for _user in self.users_ratings:
            if _user != user:
                distance = person_correlation(self.users_ratings[_user], self.users_ratings[user])
                distances.append((_user, distance))
        return sorted(distances, key=lambda coe_user: coe_user[1], reverse=True)

    def calculating_project_valuetion(self):
        """Calcule value projected"""
        pass
