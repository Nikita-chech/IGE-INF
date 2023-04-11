def f(s, p):                    # одна куча, Ваня первым после неудачного Пети
    if s >= 68 and p == 3:
        return True
    else:
        if s < 68 and p == 3:
            return False
    return f(s + 1, p + 1) or f(s + 4, p + 1) or f(s * 5, p + 1)

for i in range(1, 68):
    if f(i, 1):
        print(i)
        break
