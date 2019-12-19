a=list((input()))
k=3
i=0
s=len(a)
c=[]
d=[]
while(i<(s-(k-1))):
    c.append(a[i:(i+(k))])
    i+=1
for i in c:
    d.append(int("".join(i)))
print(min(d))
