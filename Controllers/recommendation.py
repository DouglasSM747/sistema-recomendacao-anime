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
        distances = sorted(distances, key=lambda coe_user: coe_user[1], reverse=True)
        if len(distances) > k:
            return distances[:k]
        else:
            return distances

    
    def recommend_animes_for(self, user='vitor'):
        """
        Recommend animes using k-neighbors
        """
        self.k_neighbors = self.select_kneighbors_for(user)
        print(self.k_neighbors)

        # Sum all correlations of all users
        sum = 0
        for _, rate in self.k_neighbors:
            sum += rate
        print(sum)

        
        asdf = {}
        for user_1, _ in self.k_neighbors:
            vbn = {}
            
            # run all movies for each user
            for dict_movie_rate_1 in self.users_ratings[user_1]:

                vbn[user_1] = {dict_movie_rate_1['movie']: dict_movie_rate_1['rate']}

                for user_2, _ in self.k_neighbors:
                    if user_1 != user_2:

                        # verify if has first movie
                        for dict_movie_rate_2 in self.users_ratings[user_2]:
                            
                            if dict_movie_rate_1['movie'] == dict_movie_rate_2['movie']:
                                print(user_2, dict_movie_rate_1)
                                vbn[user_2] = {dict_movie_rate_2['movie']: dict_movie_rate_2['rate']}
                                break

            if len(vbn) == len(self.k_neighbors):
                asdf.update(vbn)
        
        recommendations = []

        print(asdf)

        # create a project rating
        # project_rating = 0
        # for _user, dict_rate in asdf.items():

        #     for movie, rate in dict_rate:

        #         # get person of user
        #         person_corr = 0
        #         for u,p in self.k_neighbors:
        #             if _user == u:
        #                 person_corr = p
        #                 break
        #         project_rating += (person_corr/sum) 
                        


    def calculating_project_valuetion(self):
        """Calcule value projected"""
        pass
