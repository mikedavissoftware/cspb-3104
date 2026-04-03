s1 = "abdd"
s2 = "abcd"

print(sum(a == b for a, b in zip(s1, s2)))