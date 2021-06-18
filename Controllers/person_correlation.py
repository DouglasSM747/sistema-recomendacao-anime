from math import sqrt


def isAvaliable(r1, r2):
    communs = 0
    for movie in r2:
        if m1InM2(movie['movie'], r1) > 0:
            communs += 1
    if communs == len(r2):
        return False
    else:
        return True


def m1InM2(movie1, r2):
    for movie2 in r2:
        if movie1 == movie2['movie']:
            return movie2['rate']
    return -1000


def person_correlat1ion(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0

    if not isAvaliable(rating1, rating2):
        return -1

    for key in rating1:
        rate_m2 = m1InM2(key['movie'], rating2)
        if rate_m2 > 0:
            n += 1
            x = key['rate']
            y = rate_m2
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    if n == 0:
        return -1

    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)

    if denominator == 0:
        return -1
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator


def person_correlation(r1, r2):
    if not isAvaliable(r1, r2):
        return -1

    xiyi = 0
    xi = 0
    yi = 0
    expo_xi = 0
    expo_yi = 0
    band_common = 0

    for movie in r1:
        rate_m2 = m1InM2(movie['movie'], r2)
        if rate_m2 > 0:
            band_common += 1
            xiyi += (movie['rate'] * rate_m2)
            xi += movie['rate']
            expo_xi += pow(movie['rate'], 2)

    for movie in r2:
        rate_m1 = m1InM2(movie['movie'], r1)
        if rate_m1 > 0:
            expo_yi += pow(movie['rate'], 2)
            yi += movie['rate']

    if band_common <= 0:
        return -1

    value_xi_final = pow(xi, 2) / band_common
    value_yi_final = pow(yi, 2) / band_common

    cor_xi = sqrt(expo_xi - value_xi_final)
    cor_yi = sqrt(expo_yi - value_yi_final)

    if cor_xi * cor_yi == 0:
        return -1
    final_result = (xiyi - ((xi * yi) / band_common)) / (cor_xi * cor_yi)
    return final_result
