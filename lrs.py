def lrs(s):
    n = len(s)
    c = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1,n +1):
        for  j in range(1 , n +1):
            if s[i-1] == s[j-1] and i!=j :
                c[i][j] = 1 + c[i-1][j-1]
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])

    lrs_sequence = []

    i, j = n, n
    while i > 0 and j > 0:
        if s[i - 1] == s[j - 1] and i != j:
            lrs_sequence.append(s[i - 1])
            i -= 1
            j -= 1
        elif c[i - 1][j] >= c[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lrs_sequence.reverse()

    return c[n][n], ''.join(lrs_sequence)

s="AABEBCDD"
length , sequence = lrs(s)
print("The length of The lrs is  : ", length)
print("the sequence of the lrs is : " , sequence)






