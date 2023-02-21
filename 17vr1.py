a=open('17.txt')
n=4500
f=[]
for i in range(n):
    f.append(int(a.readline()))
cnt=0
m=-10000000
for i in range(len(f)-1):
    if (((f[i]+f[i+1])>=100) and (f[i]<0 or f[i+1]<0)):
        cnt+=1
        m=max(m, f[i]*f[i+1])
print(cnt, m)


