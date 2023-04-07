f = open('17_4414.txt')
n = 10_000
l = []

for i in range(n):
    l.append(int(f.readline()))

maxim = -10_000
cnt = 0

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] - l[j] % 36 == 0 and (l[i] % 13 == 0 or l[j] % 13 == 0):
            cnt += 1
            maxim = max(maxim, l[i] - l[j])

print(cnt, maxim)
