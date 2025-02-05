def solve(numheads, numlegs):
    for i in range(numheads):
        for j in range(numheads):
            if i + j == numheads:
                if i * 2 + j * 4 == numlegs:
                    return i, j


