class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, foods):
        current = self.root
        for food in foods:
            if food not in current.children:
                current.children[food] = TrieNode()
            current = current.children[food]

    def printTrie(self, node=None, depth=0):
        if node is None:
            node = self.root
        sortedKeys = sorted(node.children.keys())
        for key in sortedKeys:
            print('--'*depth + key)
            self.printTrie(node.children[key], depth+1)

def main():
    N = int(input())
    trie = Trie()

    for _ in range(N):
        data = input().split()
        trie.insert(data[1:])

    trie.printTrie()

if __name__ == '__main__':
    main()