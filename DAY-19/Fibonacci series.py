def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]= fib(n-1)+fib(n-2)
    return memo[n]
print(fib(9))

# Fibonacci Series With Tabulation Method
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fib(5))
