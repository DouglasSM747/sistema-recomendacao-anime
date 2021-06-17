from math import sqrt


def person_correlation(ratings_1, ratings_2):
    sum_xy  = 0
    sum_x = 0
    sum_y = 0
    sum_x_2 = 0
    sum_y_2 = 0
    n = 0
    commonRatings = False
    for key in ratings_1:
        if key in ratings_2:
            sum_xy += (ratings_1[key] * ratings_2[key])
            sum_x += ratings_1[key]
            sum_y += ratings_2[key]
            sum_x_2 += pow(ratings_1[key], 2)
            sum_y_2 += pow(ratings_2[key], 2)
            n += 1
            commonRatings = True
    
    numerator = sum_xy - ((sum_x * sum_y)/n)
    denominador = (sqrt(sum_x_2 - (pow(sum_x, 2)/n))) * (sqrt(sum_y_2 - (pow(sum_y, 2)/n)))
    
    if commonRatings and denominador != 0.0:
        return (numerator / denominador)
    
    else:
        return -1
