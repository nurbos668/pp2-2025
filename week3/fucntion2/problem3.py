def sort_with_category(movies, category):
    new_list = []

    for i in range(len(movies)):
        if movies[i]["category"] == category:
            new_list.append(movies[i])

    return new_list
