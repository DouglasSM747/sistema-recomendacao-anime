import pandas as pd

from random import randint

from Controllers.connection import Connection

animes = pd.read_csv('anime.csv')
animes = animes.sample(n=200)


def choice_names_pass(n=100):
    """Get names and passwords"""
    names = pd.read_csv('names.csv')
    unique_names = names.drop_duplicates(subset='name')
    unique_names = unique_names.sample(n=n)
    names = unique_names.name.values.tolist()
    passwords = unique_names.year.values.tolist()
    return names, passwords


def choice_animes_rates(min=10, max=20):
    """Get animes and your rates"""
    n = randint(min, max)
    animes_subset = animes.sample(n=n)
    animes_name = animes_subset.name.values.tolist()
    rates = [randint(1, 5) for _ in range(len(animes_name))]
    return animes_name, rates


def main():
    c = Connection()
    names, passwords = choice_names_pass()
    for name, password in zip(names, passwords):
        # print(f'Name={name}, password={password}')
        user_id = c.createUser(name, password)
        animes, rates = choice_animes_rates()
        for anime, rate in zip(animes, rates):
            # print(f'    Anime={anime}, rate={rate}')
            c.rate_anime(anime, user_id, rate)


if __name__ == '__main__':
    main()
