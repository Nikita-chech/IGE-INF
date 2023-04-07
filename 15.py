for a in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if ((150 != (y + 2 * x + 2 * z)) or (a < x) or (a < y) or (a < z)) == 0:
                    flag = False
                    break
    if flag == True:
        print(a)
