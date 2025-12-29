s = [2,3,4,5,6,7]

def majority_element(s):
    for num in s:
        if s.count(num) > len(s) // 2:
            return num
    return -1

print(majority_element(s))
