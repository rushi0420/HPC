from collections import deque

class Node:
	def __init__(self, 	data):
		self.data = data
		self.left = self.right = None

def insert(root, data):
	if not root:
		return Node(data)

	q = deque([root])
	while q:
		temp = q.popleft()
		if not temp.left:
			temp.left = Node(data)
			return root
		q.append(temp.left)

		if not temp.right:
			temp.right = Node(data)
			return root
		q.append(temp.right)

def bfs(root):
	if not root:
		return

	q = deque([root])
	while q:
		node = q.popleft()
		print(node.data, end=" ")
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)

root = None
n = int(input("Enter number of nodes: "))
for _ in range(n):
	data = int(input("Enter data: "))
	root = insert(root, data)

print("BFS Traversal:")
bfs(root)