def count_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    dp = [[0] * 5 for _ in range(n)]
    for i in range(5):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1))
    return sum(dp[n - 1])
    n = eval(input("enter a number:"))
print(count_strings(n))
