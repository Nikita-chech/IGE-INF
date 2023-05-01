for n in range(100):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        g = (n % 3) * 3
        s = s + bin(g)[2:]

    if int(s, 2) > 76:
        print(n)
        break
