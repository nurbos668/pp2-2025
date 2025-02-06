def avg_score(movies):
    sum_score = 0
    count_movies = 0

    for movie in movies:
        sum_score += movie["imdb"]
        count_movies += 1

    return sum_score / count_movies