from math import sqrt


def person_correlation(ratings_1, ratings_2):
    """
    Implements person correlation to calculate similarity to
    persons using your rating.
    param rantings_1 list: is a list of dicts with ratings
    to user 1
    param rantings_2 list: is a list of dicts with ratings
    to user 2
    """
    sum_xy  = 0
    sum_x = 0
    sum_y = 0
    sum_x_2 = 0
    sum_y_2 = 0
    n = 0
    commonRatings = False

    for dict_v in ratings_1:
        for dict_u in ratings_2:
            if dict_v['movie'] == dict_u['movie']:
                rate_1 = dict_v['rate']
                rate_2 = dict_u['rate']
                sum_xy += (rate_1 * rate_2)
                sum_x += rate_1
                sum_y += rate_2
                sum_x_2 += pow(rate_1, 2)
                sum_y_2 += pow(rate_2, 2)
            n += 1
            commonRatings = True
    if n != 0:
        numerator = sum_xy - ((sum_x * sum_y)/n)
        denominador = (sqrt(sum_x_2 - (pow(sum_x, 2)/n))) * (sqrt(sum_y_2 - (pow(sum_y, 2)/n)))
    else:
        return -1
    
    if (commonRatings != 0.0) and (denominador != 0.0):
        return (numerator / denominador)
    
    else:
        return -1
