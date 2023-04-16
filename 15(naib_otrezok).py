p1, p2, q1, q2 = 3, 38, 21, 57
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

def f(m, m1):
    return ((x in Q) <= (x in P)) <= (not(x in A))

A = set([i / 10 for i in range(20, 600)])
for x in [i / 10 for i in range(20, 600)]:
    if not(f(x, A)):
        A.remove(x)

print(sorted(A))