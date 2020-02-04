from itertools import combinations_with_replacement 
b=20
c=[]
for i in range(1,b//2):
    comb = combinations_with_replacement([3,5,10], i)
    c1=list(comb)
    for i in range(len(c1)):
        if(sum(c1[i]))==b:
            c.append(c1[i])
print(len(c))
 
