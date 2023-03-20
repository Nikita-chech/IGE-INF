def f(x, y):
    if x > y or x == 43:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 2, y) + f(x + (x - 1), y) + f(x + (x + 1), y)


print(f(7, 63))
