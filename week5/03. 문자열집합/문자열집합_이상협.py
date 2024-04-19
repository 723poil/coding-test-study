stdin = open('input.txt', 'r')
input = stdin.readline


class Node:
    def __init__(self, key: str, data=None):
        self.key = key
        self.data = data
        self.child = dict()


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, string: str):
        cur_node = self.root

        for ss in string:
            if ss not in cur_node.child:
                cur_node.child[ss] = Node(ss)

            cur_node = cur_node.child[ss]

        cur_node.data = string

    def check(self, string: str) -> bool:
        cur_node = self.root

        for ss in string:
            if ss not in cur_node.child:
                return False
            cur_node = cur_node.child[ss]

        if cur_node.data == string:
            return True

        return False


if __name__ == '__main__':
    N, M = map(int, input().split())
    count = 0

    trie = Trie()

    for _ in range(N):
        temp = input().rstrip()
        # 트리에 집어넣기
        trie.insert(temp)

    for _ in range(M):
        temp = input().rstrip()
        check = trie.check(temp)
        if check:
            count += 1

    print(count)
