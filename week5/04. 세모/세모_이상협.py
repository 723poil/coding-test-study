# stdin = open('input.txt', 'r')
# input = stdin.readline

if __name__ == '__main__':
    N = int(input())

    print((N-1) + ((N - 1) * (N - 2) // 2) * 2)

    for i in range(2, N+1):
        print(1, i)
    # 2 - 1
    # 3 - 4
    # 4 - (N - 1) + ((N - 1) (N - 2) / 2) * 2