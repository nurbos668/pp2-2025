def has_33(lst):
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            return True

    return False


