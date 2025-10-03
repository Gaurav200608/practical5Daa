def LCS(X, Y):
    m = len(X)
    n = len(Y)


    dp = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    length_of_lcs = dp[m][n]
   
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1


    lcs.reverse()
    lcs_string = ''.join(lcs)


    return dp, length_of_lcs, lcs_string


X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"


dp_matrix, length, lcs_string = LCS(X, Y)


print("Cost matrix:")
for row in dp_matrix:
    print(row)


print("\nLength of LCS:", length)
print("LCS:", lcs_string)
