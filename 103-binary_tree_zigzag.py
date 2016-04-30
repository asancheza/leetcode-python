#!/usr/bin/python

class TreeNode:
	val = ""
	left = None
	right = None

	def __init__(self, val):
		self.val = val

def zigzag(root):
	stack = [root]

	result = []
	order = "Right"
	level = 0
	levels = {}

	while stack:
		nextlevel = []

		for node in stack:
			if level in levels:
				levels[level].append(node.val)
			else:
				levels[level] = [node.val]

			if order == "Left":
				if node.left:
					nextlevel.append(node.left)

				if node.right:
					nextlevel.append(node.right)

				order = "Right"
			else:
				if node.left:
					nextlevel.append(node.right)

				if node.right:
					nextlevel.append(node.left)

				order = "Left"

		level = level + 1
		stack = nextlevel

	return levels

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print zigzag(root)