from collections import deque

def is_it_a_tree(node_count, edge_start, edge_end):
    adjList = [[] for _ in range(node_count)]
    
    for i in range(len(edge_start)):
        adjList[edge_start[i]].append(edge_end[i])
        adjList[edge_end[i]].append(edge_start[i])
    
    #print(adjList)
    visited = [-1] * node_count
    parent = [-1] * node_count
    
    def dfs(source):
        visited[source] = 1
        for neighbor in adjList[source]:
            if visited[neighbor] == -1:
                parent[neighbor] = source
                if dfs(neighbor):
                    return True
                else:
                    if parent[source] != neighbor:
                        return True
        return False

    def bfs(source):
    	visited[source] = 1
    	q = deque([source])
    	while q:
    		node = q.popleft()
    		for neighbor in adjList[node]:
    			if visited[neighbor] == -1:
    				visited[neighbor] = 1
    				parent[neighbor] = node
    				q.append(neighbor)
    			else:
    				if parent[node] != neighbor:
    					return True
    	return False
    
    components = 0
    for v in range(node_count):
        if visited[v] == -1:
            components += 1
            if components > 1:
            	return False
            if bfs(v):
            	return False
    return True

print(is_it_a_tree(4, [0,0,0], [1,2,3])) # true
print(is_it_a_tree(6, [4, 4, 4, 2, 1], [3, 5, 0, 0, 0])) # true
print(is_it_a_tree(4, [0, 2, 0], [3, 1, 1])) # true
print(is_it_a_tree(7, [4, 5, 5, 3, 5, 6], [0, 2, 6, 4, 0, 1]))

# {
# "node_count": 6,
# "edge_start": [4, 4, 4, 2, 1],
# "edge_end": [3, 5, 0, 0, 0]
# }


# {
# "node_count": 4,
# "edge_start": [0, 2, 0],
# "edge_end": [3, 1, 1]
# }

# {
# "node_count": 7,
# "edge_start": [4, 5, 5, 3, 5, 6],
# "edge_end": [0, 2, 6, 4, 0, 1]
# }