"""
recursion error 났음 => recursionlimit 늘리기
"""

class Node:
    def __init__(self, value=None) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        
        current_node = self.root
        
        while True:
            if current_node == None:
                self.root = Node(value)
                break
            
            if current_node.value > value:
                if current_node.left == None:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left

            elif current_node.value < value:
                if current_node.right == None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right


def postorder(node):
    if node != None:
        if node.left != None:
            postorder(node.left)
        if node.right != None:
            postorder(node.right)
        print(node.value)
        

import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.read
data = [int(i) for i in input().splitlines()]

bst = BinarySearchTree()
for v in data:
    bst.insert(v)

postorder(bst.root)


