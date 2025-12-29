import math

def helper(n, r):
    res = math.factorial(n-1) // (math.factorial(n-r) * math.factorial(r-1))
    return res

for i in range(1, 10):
    for j in range(1, i+1):
        print(helper(i, j), end=" ")
    print()
