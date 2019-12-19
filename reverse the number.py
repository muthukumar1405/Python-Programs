n=int(input())
c=n+3
temp=c
for i in range(n,0,-1):
    for j in range(i):
        print(temp,end=" ")
        temp=temp+1
    temp=c-(i-1)
    c=temp
    print()
