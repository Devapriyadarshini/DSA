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

# The space complexity of this code is o(1)

def fib(n):
    if n <= 1:
        return n
    
    # We only store the two previous numbers, not the whole sequence
    prev2 = 0  # Represents dp[i-2]
    prev1 = 1  # Represents dp[i-1]
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1   # Move the pointer forward
        prev1 = current # Move the pointer forward
        
    return prev1

print(fib(9))
