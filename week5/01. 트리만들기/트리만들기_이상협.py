from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())

    node = 0
    count = m-1
    for i in range(1, n):
        if m == 2:
            print(node, i)
            node += 1
        else:
            print(node, i)
            node += 1
            if count:
                node -= 1
                count -= 1