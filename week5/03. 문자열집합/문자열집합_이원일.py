import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True
    
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

def main(set_s:list, check_words:list)->list:
    
    # 예제 입력을 바탕으로 트라이 구조 테스트
    trie = Trie()
    
    # 집합 S의 문자열을 트라이에 추가
    for word in set_s:
        trie.insert(word)

    # 트라이에서 각 문자열 검색
    count = 0
    for word in check_words:
        if trie.search(word):
            count += 1
            
    return count  # 출력 결과 반환: S에 속한 M개 문자열 중 몇 개가 포함되어 있는지
    
if __name__=="__main__":
    input = sys.stdin.readline
    n, m = map(int, input().strip().split())
    # 집합 S에 포함된 문자열들
    set_s = [input().strip() for _ in range(1, n+1)]
    # 검사해야 하는 문자열들
    check_words = [input().strip() for _ in range(n+1, n+m+1)]

    ret = main(set_s, check_words)
    print(ret)