from math import sqrt

def computerSimilarity(item_1, item_2, userRatings):
    """ Implements adjust cosseno Similarity"""
    avergares = {}
    for (key, ratings) in userRatings.items():
        avergares[key] = (float(sum(ratings.valeus()))) / len(ratings.values())
    
    num = 0
    dem1 = 0
    dem2 = 0

    for (user, rantings) in userRatings.items():
        if item_1 in rantings and item_2 in rantings:
            avg = avergares[user]
            num += (rantings[item_1] - avg) * (rantings[item_2] - avg)
            dem1 += (rantings[item_1] - avg)**2
            dem2 += (rantings[item_2] - avg)**2
    return num/(sqrt(dem1)*sqrt(dem2))
