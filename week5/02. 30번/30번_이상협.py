
# stdin = open('input.txt', 'r')
# input = stdin.readline

if __name__ == '__main__':
    T = int(input())

    for t in range(T):
        nodes = list(map(int, input().split()))

        while nodes[0] != nodes[1]:
            if nodes[0] > nodes[1]:
                nodes[0] //= 2
            elif nodes[0] < nodes[1]:
                nodes[1] //= 2

        print(10 * nodes[0])