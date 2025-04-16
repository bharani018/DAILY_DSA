def ClimbingTrees(n):
    if n<=2:
        return n
    ns = [0] * (n+1)
    ns[1], ns[2] = 1, 2
    for i in range(3, n+1):
        ns[i] = ns[i-1] + ns[i-2]
    return ns[n]

n = 4
print(ClimbingTrees(n))