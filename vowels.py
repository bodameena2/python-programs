s = "studying"

vowel_count = 0
consonant_count = 0

for char in s:
    if char in "aeiouAEIOU":
        vowel_count += 1
    else:
        consonant_count += 1

print("vowel", vowel_count)
print("consonant", consonant_count)
