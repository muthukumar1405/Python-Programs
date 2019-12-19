a=list(input().split(' '))
vowels='aeiou'
for i in range(len(a)):
    s=(a[i])
    c=[]
    for j in (s):
        c.append(j)
        if(c[0] not in vowels):
            print(s[1:5]+s[0]+'ma'+'a'*(i+1),end=" ")
            break
        elif(c[0] in vowels):
            print(s+'ma'+'a'*(i+1),end=" ")
            break
