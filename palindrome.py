s="madam"
res=""
for i in range(len(s)):
 res=s[i]+res
if s==res:
    print("palindrome")
else:
    print("not a palindrome")
