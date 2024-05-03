def main(N, S, sequences):
    cnt = 0

    def subSequence(idx, sum):
        nonlocal cnt
        # 종료 조건
        if idx == N:
            if sum == S:
                cnt += 1
            return
        # 재귀 확장
        subSequence(idx+1, sum+sequences[idx])
        subSequence(idx+1, sum)

    subSequence(0, 0)
    if S == 0:
        print(cnt-1)
    else:
        print(cnt)

if __name__ == '__main__':
    N, S = map(int, input().split())
    sequences = list(map(int, input().split()))
    main(N, S, sequences)
