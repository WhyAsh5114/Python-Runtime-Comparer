class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printPreorder(root):

	if root:

		print(root.val),

		printPreorder(root.left)

		printPreorder(root.right)

if __name__ == "__main__":
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Preorder traversal of binary tree is"
printPreorder(root)
