def get_maximum_profit(price):
    rodlen = len(price)
    prices = [0] + price
    dp = [0] * (rodlen + 1)
    dp[0] = 0
    dp[1] = prices[1]
    for length in range(1, rodlen + 1):
    	result = 0
    	for cut in range(1, length + 1):
    		result = max(result, prices[cut] + dp[length - cut])
    	dp[length] = result
    return dp[rodlen]

print(get_maximum_profit([1,5,8,9])) # 10
print(get_maximum_profit([8,4,2])) # 24
print(get_maximum_profit([3, 7, 2, 6, 6])) # 17
print(get_maximum_profit([3, 3, 3, 3, 3])) # 15
print(get_maximum_profit([5, 4, 3, 2, 1])) # 25