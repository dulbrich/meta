from collections import deque

def count_change(coins, amount):
	if len(coins) == 0:
		return 0
	answer = 0
	dp = set()
	q = deque([0])
	while q:
		level_node_count = len(q)
		for i in range(level_node_count):
			node_sum = q.popleft()
			dp.add(node_sum)
			for coin in coins:
				if node_sum + coin > amount:
					continue
				if node_sum + coin in dp:
					continue
				if node_sum + coin == amount:
					answer += 1
					continue
				q.append(node_sum + coin)

	return answer

print(count_change([1,2,3], 3)) # 3
print(count_change([9, 1, 8, 10, 3], 12)) # 10
print(count_change([1, 2, 3, 4, 5], 15)) # 84


# { # answer = 10
# "coins": [9, 1, 8, 10, 3],
# "amount": 12
# }

# { # answer = 84
# "coins": [1, 2, 3, 4, 5],
# "amount": 15
# }