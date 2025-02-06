def sublist(movies):
    new_list = []

    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            new_list.append(movies[i])

    return new_list
