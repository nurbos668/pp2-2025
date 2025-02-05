def filter_prime(numbers):
    new_list = []

    for num in numbers:
        cnt = 0
        for i in range(1, int(num) + 1):
            if int(num) % i == 0:
                cnt += 1
        if cnt == 2:
            new_list.append(int(num))

    return new_list


