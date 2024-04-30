def main(N, M, ns):
    result = []
    visited = [False] * (N+1)
    finalResult = set()

    def permutation(depth):
        if depth == M:
            # finalResult.add(result) 안되는 이유
            # set은 불변 객체만 추가할 수 있기 때문
            finalResult.add(tuple(result))
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                result.append(ns[i])
                permutation(depth+1)
                visited[i] = False
                result.pop()

    permutation(0)
    sortedFinalResult = sorted(finalResult)
    for r in sortedFinalResult:
        print(' '.join(map(str, r)))


if __name__ == '__main__':
    N, M = map(int, input().split())
    ns = list(map(int, input().split()))
    main(N, M, ns)
