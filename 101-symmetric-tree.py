#!/usr/bin/python

def symmetric(Tree):
  if Tree == None:
    return True

  return _symmetric(tree.left, tree.right)

def _symmetric(left, right):
  if left == None and right == None:
    return True

  if left == None or right == None:
    return False

  if left.value == right.value and _symmetric(left.left, right.right) and _symmetric(left.right, right.left):
    return True

  return False

class Tree: 
  value = ""
  left = None
  right = None

  def __init__(self, value):
    self.value = value

tree = Tree(5)
tree.left = Tree(2)
tree.right = Tree(2)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.right.left = Tree(5)
tree.right.right = Tree(2)

print symmetric(Tree)
