a=input()
vowels="aeiou"
word=list(a)
i=0
j=len(word)-1
while(i<j):
    if(word[i] not in vowels):
        i+=1
    elif(word[j] not in vowels):
        j-=1
    else:
        word[i],word[j]=word[j],word[i]
        i+=1
        j-=1
print("".join(word))


