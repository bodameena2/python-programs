s = [-1,3,8,9,2,10,0,6]

res = s[0]
count = s[0]

for i in range(1, len(s)):
    count = max(s[i], count + s[i])
    res = max(res, count)

print(res)
