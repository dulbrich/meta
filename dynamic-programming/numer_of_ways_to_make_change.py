def number_of_ways(coins: list[int], amount: int):
	dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
	
	# initialize the base cases
	for row in dp:
		row[0] = 1

	for row in range(1, len(coins) + 1):
		for col in range(amount + 1):
			if col - coins[row - 1] < 0:
				dp[row][col] = dp[row - 1][col]
			else:
				dp[row][col] = dp[row - 1][col] + dp[row][col - coins[row - 1]]
	
	return dp[len(coins)][amount]

print(number_of_ways([9,1,8,10,3], 12))
print(number_of_ways([1,2,3], 3))