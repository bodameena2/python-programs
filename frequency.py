s = "meenu"
res = {}
for char in s:
    if char in res:
        res[char] = res[char] + 1
    else:
        res[char] = 1
print(res)
