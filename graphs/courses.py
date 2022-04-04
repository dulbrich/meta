from collections import deque

def get_class_order(n: int, prerequisites: list[list[int]]):
	adjlist = [[] for _ in range(n)]
	for (src, dst) in prerequisites:
		adjlist[dst].append(src)

	visited = [-1] * n
	timestamp = [0]
	arrival = [-1] * n
	departure = [-1] * n
	topsort = []

	def dfs(source: int):
		arrival[source] = timestamp[0]
		timestamp[0] += 1
		visited[source] = 1
		for neighbor in adjlist[source]:
			if visited[neighbor] == -1:
				if dfs(neighbor):
					return True
			else:
				if departure[neighbor] == -1:
					return True
		departure[source] = timestamp[0]
		timestamp[0] += 1
		topsort.append(source)
		return False

	for v in range(n):
		if visited[v] == -1:
			if dfs(v):
				return []
	topsort.reverse()
	return topsort

def can_i_graduate(n: int, prerequisites: list[list[int]]):
	adjlist = [[] for _ in range(n)]
	for (src, dst) in prerequisites:
		adjlist[dst].append(src)

	visited = [-1] * n
	timestamp = [0]
	arrival = [-1] * n
	departure = [-1] * n

	def dfs(source: int):
		arrival[source] = timestamp[0]
		timestamp[0] += 1
		visited[source] = 1
		for neighbor in adjlist[source]:
			if visited[neighbor] == -1:
				if dfs(neighbor):
					return True
			else:
				if departure[neighbor] == -1:
					return True
		departure[source] = timestamp[0]
		timestamp[0] += 1
		return False

	for v in range(n):
		if visited[v] == -1:
			if dfs(v):
				return False
	return True

def can_be_completed(n, a, b):
    adjlist = [[] for _ in range(n)]
    for i, dst in enumerate(a):
        adjlist[dst].append(b[i])
    
    visited = [-1] * n
    timestamp = [0]
    arrival = [-1] * n
    departure = [-1] * n
    
    def dfs(source: int):
        arrival[source] = timestamp[0]
        timestamp[0] += 1
        visited[source] = 1
        for neighbor in adjlist[source]:
            if visited[neighbor] == -1:
                if dfs(neighbor):
                	return True
            else:
                if departure[neighbor] == -1:
                	return True
        departure[source] = timestamp[0]
        timestamp[0] += 1
        return False
        
    for v in range(n):
	    if visited[v] == -1:
	    	if dfs(v):
	            return False
    return True

print(can_be_completed(4, [1, 1, 3, 0], [0, 2, 1, 3]))
print(can_be_completed(3, [0, 1, 2], [1, 2, 0]))

# should be false
# {
# "n": 4,
# "a": [1, 1, 3, 0],
# "b": [0, 2, 1, 3]
# }

# should be false
# {
# "n": 3,
# "a": [0, 1, 2],
# "b": [1, 2, 0]
# }