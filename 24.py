n = open('17_4414.txt')
g=10000
l=[]
for i in range(g):
    l.append(int(n.readline()))

maxim, cnt = 0, 0

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if (l[i] - l[j]) % 36 == 0 and (l[i] % 13 == 0 or l[j] % 13 == 0):
            cnt += 1
            maxim = max(maxim, abs(l[i] - l[j]))

print(maxim, cnt)
