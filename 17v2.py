f=open('17.txt')
n=5000
l=[]
for i in range(n):
    l.append(int(f.readline()))
m=0
c=0
m2=0
for i in l:
    if l[i]%11==0:
        m=max(m, l[i])
for i in range(len(l)-1):
    if (l[i]%11==0 and l[i]+l[i+1]<=m) or (l[i+1]%11==0 and l[i]+l[i+1]<=m):
        c+=1
        m2=max(m2, l[i]+l[i+1])
print(c, m2)