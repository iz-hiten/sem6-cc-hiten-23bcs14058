import sys
input=sys.stdin.readline
n,m=map(int,input().split())
p=list(range(n+1))
def f(x):
    while p[x]!=x:
        p[x]=p[p[x]]
        x=p[x]
    return x
for _ in range(m):
    a,b=map(int,input().split())
    a=f(a);b=f(b)
    if a!=b:p[a]=b
r=[]
for i in range(1,n+1):
    if f(i)==i:r.append(i)
print(len(r)-1)
for i in range(len(r)-1):
    print(r[i],r[i+1])
