from collections import deque

def can_be_divided(num_of_people, dislike1, dislike2):
	n = num_of_people
	adjlist = [[] for _ in range(n)]

	for i in range(len(dislike1)):
		adjlist[dislike1[i]].append(dislike2[i])
		adjlist[dislike2[i]].append(dislike1[i])

	visited = [-1] * n
	parent = [-1] * n
	distance = [-1] * n

	def bfs(source):
		visited[source] = 1
		distance[source] = 0
		q = deque([source])
		while q:
			node = q.popleft()
			for neighbor in adjlist[node]:
				if visited[neighbor] == -1:
					visited[neighbor] = 1
					parent[neighbor] = node
					distance[neighbor] = distance[node] + 1
					q.append(neighbor)
				else:
					if parent[node] != neighbor:
						#Cycle
						if distance[node] == distance[neighbor]:
							return False
		return True

	for v in range(n):
		if visited[v] == -1:
			if bfs(v) == False:
				return False
	return True


print(can_be_divided(5, [0, 1, 1, 2, 3], [2, 2, 4, 3, 4])) # true
print(can_be_divided(4, [0, 0, 0, 1, 2], [1, 2, 3, 2, 3])) # false

# Should be true
# {
# "num_of_people": 5,
# "dislike1": [0, 1, 1, 2, 3],
# "dislike2": [2, 2, 4, 3, 4]
# }

# should be false
# {
# "num_of_people": 4,
# "dislike1": [0, 0, 0, 1, 2],
# "dislike2": [1, 2, 3, 2, 3]
# }