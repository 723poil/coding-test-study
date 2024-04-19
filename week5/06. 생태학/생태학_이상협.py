from sys import stdin

input = stdin.readline

class Node:
    
    def __init__(self, key: str) -> None:
        self.key = key
        self.data = None
        self.child = dict()
        self.count = 0
        
    def find(self, total: int):
        if self.data is not None:
            print(f"{self.data} {(self.count / total) * 100:.4f}")
            
        for key in sorted(self.child):
            self.child[key].find(total)
        
class Trie:
    
    def __init__(self) -> None:
        self.root = Node(None)
        
    def insert(self, string: str):
        cur_node = self.root
        
        for sub in string:
            if not cur_node.child.get(sub):
                cur_node.child[sub] = Node(sub)
            
            cur_node = cur_node.child[sub]
        
        cur_node.data = string
        cur_node.count += 1
        
    def search(self, total: int):
        cur_node = self.root
        
        cur_node.find(total)
        
            

if __name__ == '__main__':
    
    trie = Trie()
    total = 0
    
    ss = input().rstrip()
    
    while ss:
        total += 1
        trie.insert(ss)
        
        ss = input().rstrip()
        
    trie.search(total)