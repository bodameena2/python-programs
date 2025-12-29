s=[1,-2,3,-4,5,-6]
def rearrange_alternately(s):
    if len(s)%2!=0:
        return-1
    i=0
    j=1
    while j<=len(s):
        s[i],s[j]=s[j],s[i]
        i+=2
        j+=2
        return s
print(rearrange_alternately(s))
