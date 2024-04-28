import sys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

def buildTree(preorder):
    root = Node(preorder[0])
    for key in preorder[1:]:
        insert(root, key)
    return root

# 런타임에러(RecursionError)
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline
preorder = []
while True:
    line = input().strip()
    if not line:
        break
    preorder.append(int(line))
root = buildTree(preorder)
postorder(root)
