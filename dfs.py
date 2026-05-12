# Graph using adjacency list
graph = {}


# DFS function
def dfs(node, visited):
	visited.add(node)
	print(node, end=" ")
	for adj in graph[node]:
		if adj not in visited:
			dfs(adj, visited)


# Main
n, m, start = map(int, input("Enter nodes, edges, start node: ").split())

# Initialize graph
for i in range(n):
	graph[i] = []

print("Enter edges (u v):")
for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

visited = set()
print("DFS Traversal:", end=" ")
dfs(start, visited)