import problem3

def avg_score_category(movies, category):
    sum_score = 0
    cnt = 0

    new_list = problem3.sort_with_category(movies, category)

    for movie in new_list:
        sum_score += movie["imdb"]
        cnt += 1

    return sum_score / cnt