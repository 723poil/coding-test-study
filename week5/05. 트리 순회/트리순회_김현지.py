class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def buildTree(root, left, right):
    if root not in tree:
        tree[root] = Node(root)
    if left != '.':
        tree[left] = Node(left)
        tree[root].left = tree[left]
    if right != '.':
        tree[right] = Node(right)
        tree[root].right = tree[right]
    return tree

def preorder(node):
    if node is None or node.data == '.':
        return ''
    return node.data + preorder(node.left) + preorder(node.right)

def inorder(node):
    if node is None or node.data == '.':
        return ''
    return inorder(node.left) + node.data + inorder(node.right)

def postorder(node):
    if node is None or node.data == '.':
        return ''
    return postorder(node.left) + postorder(node.right) + node.data


N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    buildTree(root, left, right)

root = tree['A']
print(preorder(root))
print(inorder(root))
print(postorder(root))
