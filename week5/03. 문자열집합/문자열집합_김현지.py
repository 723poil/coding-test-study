class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isEndOfWord = True

    def search(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.isEndOfWord

def countIncludedStrings():
    N, M = map(int, input().split())

    trie = Trie()

    # 집합 S에 포함된 문자열을 트라이에 삽입
    for _ in range(N):
        trie.insert(input())

    # 검사해야 할 문자열들의 포함 여부 검사
    count = 0
    for _ in range(M):
        if trie.search(input()):
            count += 1

    return count

print(countIncludedStrings())
