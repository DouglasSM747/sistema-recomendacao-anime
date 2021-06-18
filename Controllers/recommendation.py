import json

from pprint import pprint

from Controllers.connection import Connection
from .person_correlation import person_correlation


class Recommendation:
    def __init__(self):
        self.data_base_connection = Connection()
        self.users_ratings = self.data_base_connection.get_json()
        self.users_ratings = json.loads(self.users_ratings)

    def select_kneighbors_for(self, user, k):
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
        positive_distances = list(filter(lambda x: x[1] > 0, distances))
        if len(positive_distances) > k:
            return positive_distances[:k]
        else:
            return positive_distances

    def knn_recomendation(self, user, k):
        k_neigh = self.select_kneighbors_for(user=user, k=k)

        sum_pearson = 0
        for i in range(len(k_neigh)):
            sum_pearson += k_neigh[i][1]
        influence = dict()
        for i in range(len(k_neigh)):
            peso = k_neigh[i][1] / sum_pearson
            influence[k_neigh[i][0]] = peso
        return self.calculating_project_rating(k_neigh, influence)

    def calculating_project_rating(self, users, influence):
        res = self.data_base_connection.getUsers()
        name_users = []
        for i in users:
            name_users.append(i[0])

        id_users = list(filter(lambda x: x[1] in name_users, res))

        users_animes = dict()

        for i in id_users:
            animes = self.data_base_connection.get_animes_user(i[0])
            users_animes[i[1]] = animes

        anime_aparicion = dict()

        # Verifica os Animes Comuns a Todos
        for i in users_animes:
            for j in users_animes[i]:
                if j[0] not in anime_aparicion.keys():
                    anime_aparicion[j[0]] = 1
                else:
                    anime_aparicion[j[0]] += 1

        animes_comuns = []
        # Informando Animes Comuns A Todos
        for i in anime_aparicion:
            if anime_aparicion[i] == len(users_animes):
                animes_comuns.append(i)

        list_rating = []
        # Calculando Rating para cada Anime Comum
        for i in animes_comuns:
            projected_rate = 0
            for j in name_users:
                projected_rate += (self.__get_rate_in_anime_user(anime=i, user_animes=users_animes[j]) * influence[j])
            list_rating.append((i, projected_rate))
        return list_rating

    def __get_rate_in_anime_user(self, anime, user_animes):
        for i in user_animes:
            if i[0] == anime:
                return i[1]

    def calculating_project_valuetion(self):
        """Calcule value projected"""
        pass
