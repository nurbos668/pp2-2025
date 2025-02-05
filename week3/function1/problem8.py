def spy_game(lst):
    for i in range(len(lst) - 2):
        if lst[i] == 0 and lst[i + 1] == 0 and lst[i + 2] == 7:
            return True

    return False

