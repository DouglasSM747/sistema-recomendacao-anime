import csv

from Controllers.connection import Connection
from Screens.screens import *
from functools import partial
from Structs.User import User
from Controllers.recommendation import Recommendation

recomen = Recommendation()

anime_list = []

anime_list_user = []

m_connection = Connection()

m_user = User("", "")


def selected_screen(choice):
    clear()
    if choice == "Criar Conta":
        res = createAccount()
        m_connection.createUser(res['login'], res['password'])
        init_login()


def recomend():
    reco = Recommendation()
    lista = reco.knn_recomendation(user=m_user.getLogin(), k=2)
    aux_list_reco = [['Anime Recomendado', 'Avaliação']]
    if len(lista) > 0:
        for i in range(len(lista)):
            aux_list_reco.append(
                [
                    str(lista[i][0]),
                    str(lista[i][1])
                ]
            )
        put_table(aux_list_reco)


def init_login():
    global anime_list_user
    res = login()
    result_get_user = m_connection.get_user(res['login'], res['password'])
    if result_get_user is not None:
        global m_user
        m_user = User(res['login'], result_get_user['id'])
        anime_list_user = m_connection.get_animes_user(m_user.getId())
        clear()
        recomend()
        mainPage()
    else:
        initial_screen()


def initial_screen():
    clear()
    put_buttons(['Criar Conta'], onclick=partial(selected_screen))
    init_login()


def addNota(choice, anime):
    m_connection.rate_anime(anime, m_user.getId(), int(choice))

    anime_exist = False
    for i in range(len(anime_list_user)):
        if anime_list_user[i][0] == anime:
            anime_list_user[i] = (anime, choice)
            anime_exist = True
            break

    if not anime_exist:
        anime_list_user.append((anime, choice))


def load_anime_interface(m_list_anime):
    aux_list_interface = [['Anime', 'Avaliação']]

    for i in range(len(m_list_anime)):
        aux_list_interface.append(
            [
                m_list_anime[i],
                put_buttons(['1', '2', '3', '4', '5'], onclick=partial(addNota, anime=m_list_anime[i]))
            ]
        )
    put_table(aux_list_interface)


def load_csv():
    with open('anime.csv', 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            anime_list.append(row[1])


def mainPage():
    anime_search = input("Informe o nome do anime que deseja buscar")
    clear()
    aux_anime_list = []
    for anime_name in anime_list:
        if anime_search in anime_name:
            if len(anime_name) > 60:
                aux_anime_list.append(anime_name[0:60])
            else:
                aux_anime_list.append(anime_name)
    load_anime_interface(aux_anime_list)
    mainPage()


if __name__ == '__main__':
    load_csv()
    initial_screen()
