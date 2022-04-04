from queue import Queue

visited = [False] * n

def build_graph(n: int, edges: list[list[int]]):
	adjList = [None] * n
	for edge_src, edge_dst in edges:
		adjList[edge_src].append(edge_dst)
		adjList[edge_dst].append(edge_src)

def bfs(source: int):
	q = Queue()
	q.put(source)
	while q:
		v = q.get()
		for w in adjList[v]:
			if !visited[w]:
				visited[w] = True
				q.put(w)

def comp_count():
	num_components = 0
	for v in adjList:
		if