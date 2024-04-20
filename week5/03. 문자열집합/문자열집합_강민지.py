"""
[풀이1] set 사용하기
시간 복잡도 줄이기
- list 대신 set 사용 (자료형에 따라 시간복잡도가 다름)
- list 탐색 => O(N) / set 탐색 => O(1)
"""

# n, m = map(int, input().split())

# s_list = [input() for _ in range(n)] # 중복 불가
# answer = 0
# for _ in range(m):
#     word = input()
#     if word in s_list:
#         answer += 1

# print(answer)


#======================================================
"""
[풀이2] Trie로 구현
- 문자열 저장, 검색에 효율적인 방법
- 공통 접두사를 사용해서 메모리 사용 최적화됨
- dictionary로 Node class 구현
- Trie class에 insert, search method 구현
- input을 sys.stdin.read().splitlines()로 안하면 시간초과
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node.is_end_of_word

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, M = map(int, data[0].split())
    trie = Trie()
    
    # S 집합 구축
    for i in range(1, N+1):
        trie.insert(data[i])

    # M개 문자열 검색
    count = 0
    for j in range(N+1, N+M+1):
        if trie.search(data[j]):
            count += 1
    
    # 결과 출력
    print(count)

solve()

