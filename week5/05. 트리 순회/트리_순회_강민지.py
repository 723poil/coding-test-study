"""
BinarySearchTree 순회는 암기!
직관적인 설명 : https://brunch.co.kr/@qqplot/131
# 이진탐색트리, 이진검색트리, traverse 
"""
class Node:
    def __init__(self, value=None) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def search_node(self, value):
        return self._search_node(self.root, value)

    def _search_node(self, node, value):
        if node == None:
            return None
        
        if node.value == value:
            return node
        if node.left != None:
            node_left = self._search_node(node.left, value)
        
            if node_left != None:
                return node_left
        
        return self._search_node(node.right, value)


def preorder(node, memo=[]):
    """루트 -> 왼쪽 -> 오른쪽"""
    if node != None:
        memo.append(node.value)
        if node.left != None:
            preorder(node.left, memo)
        if node.right != None:
            preorder(node.right, memo)
    return memo
        
def inorder(node, memo=[]):
    """왼쪽 -> 루트 -> 오른쪽"""
    if node != None:
        if node.left != None:
            inorder(node.left, memo)
        memo.append(node.value)
        if node.right != None:
            inorder(node.right, memo)
    return memo

def postorder(node, memo=[]):
    """왼쪽 -> 오른쪽 -> 루트"""
    if node != None:
        if node.left != None:
            postorder(node.left, memo)
        if node.right != None:
            postorder(node.right, memo)
        memo.append(node.value)
    return memo


def main():
    from collections import deque
    n = int(input())
    insert_data = deque([input().split() for _ in range(n)])
    bst = BinarySearchTree()
    value, left, right = insert_data.popleft()
    
    bst.root = Node(value)
    if left != '.':
        bst.root.left = Node(left)
    if right != '.':
        bst.root.right = Node(right)
    
    while insert_data:
        value, left, right = insert_data.popleft()
        current_node = bst.search_node(value)
        if left != '.':
            current_node.left = Node(left)
        if right != '.':
            current_node.right = Node(right)

    print(''.join(preorder(bst.root)))
    print(''.join(inorder(bst.root)))
    print(''.join(postorder(bst.root)))
    

main()