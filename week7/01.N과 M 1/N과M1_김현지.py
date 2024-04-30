def main(N, M):
    result = []
    visited = [False] * (N+1)

    def permutation(depth):
        if depth == M:
            print(' '.join(map(str, result)))
            return
        for i in range(1, N+1):
            if visited[i] == False:
                visited[i] = True
                result.append(i)
                permutation(depth+1)
                visited[i] = False
                result.pop()

    permutation(0)


if __name__ == '__main__':
    N, M = map(int, input().split())
    main(N, M)
