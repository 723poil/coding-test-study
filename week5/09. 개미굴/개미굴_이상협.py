from sys import stdin

input = stdin.readline

def printH(level: int):
    for _ in range(level):
        print('--', end='')

class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.child = dict()
        
    def print(self, level: int = 0):
            
        childs = sorted(self.child.keys())
        
        for child in childs:
            printH(level)
            print(child)
            self.child[child].print(level + 1)
        
class Tree:
    
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, nodes: list):
        cur_node = self.root
        
        for node in nodes:
            if node not in cur_node.child:
                cur_node.child[node] = Node(node)
            
            cur_node = cur_node.child[node]
            

if __name__ == '__main__':
    N = int(input())
    
    tree = Tree()
    
    for _ in range(N):
        input_data = list(map(str, input().rstrip().split()))
        tree.insert(input_data[1:])
        
    tree.root.print()