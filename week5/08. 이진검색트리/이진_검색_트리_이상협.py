from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

input = stdin.readline

class Node:
    
    def __init__(self, data: int = None) -> None:
        self.data = data
        self.lc = None
        self.rc = None
        
class Tree:
    
    def __init__(self, data: int) -> None:
        self.root = Node(data)
        
    def insert(self, data: int):
        cur_node = self.root
        
        child = cur_node.lc if data < cur_node.data else cur_node.rc
        
        while child:
            cur_node = child
            child = cur_node.lc if data < cur_node.data else cur_node.rc
            
        if data < cur_node.data:
            cur_node.lc = Node(data)
        else:
            cur_node.rc = Node(data)
            
    def print(self, node: Node):
        if not node:
            return
        
        self.print(node.lc)
        self.print(node.rc)
        print(node.data)
            

if __name__ == '__main__':
    
    n = int(input())
    tree = Tree(n)
    
    n = input()
    while n:
        tree.insert(int(n))
        
        n = input()
       
    tree.print(tree.root)