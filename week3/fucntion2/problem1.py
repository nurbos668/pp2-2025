def above(movies, name_movie):
    for movie in movies:
        if movie["name"] == name_movie and movie["imdb"] > 5.5:
            return True

    return False

