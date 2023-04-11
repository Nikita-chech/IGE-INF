def f(s, p):                    # одна куча, Петя вторым ходом, 2 значения 
    if s >= 68 and p == 4:
        return True
    else:
        if s < 68 and p == 4:
            return False
        else:
            if s >= 68:
                return False
    if p % 2 == 1:
        return f(s + 1, p + 1) or f(s + 4, p + 1) or f(s * 5, p + 1)
    else:
        return f(s + 1, p + 1) and f(s + 4, p + 1) and f(s * 5, p + 1)

for i in range(1, 68):
    if f(i, 1):
        print(i)