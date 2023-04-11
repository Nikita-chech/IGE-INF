from functools import lru_cache

@lru_cache(None)
def f(s, p):
    if s >= 78 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(s + 1, p + 1) or f(s + 4, p + 1) or f(s * 4, p + 1)
    else:
        return f(s + 1, p + 1) and f(s + 4, p + 1) and f(s * 4, p + 1)

for i in range(1, 78):
    if f(i, 1):
        print(i)