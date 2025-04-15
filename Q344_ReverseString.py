s = ["h","e","l","l","o"]
res = []
def ReverseString(s):
    for i in range(len(s)-1, -1, -1):
        res.append(s[i])
    return res
print(ReverseString(s))