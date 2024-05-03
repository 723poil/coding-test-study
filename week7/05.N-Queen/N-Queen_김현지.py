def main(N):
    cols = [False] * N
    diag1 = [False] * (2*N-1) # 왼쪽 아래로 향하는 대각선
    diag2 = [False] * (2*N-1) # 오른쪽 아래로 향하는 대각선
    cnt = 0

    def place(row):
        nonlocal cnt
        if row == N:
            cnt += 1
        for col in range(N):
            # 왼쪽 아래 -> row+col 동일
            # 오른쪽 아래 -> row-col 동일
            ## 음수가 되면 안되어서 N-1 더함
            if not cols[col] and not diag1[row+col] and not diag2[row-col+N-1]:
                cols[col], diag1[row+col], diag2[row-col+N-1] = True, True, True
                place(row+1)
                cols[col], diag1[row+col], diag2[row-col+N-1] = False, False, False
    place(0)
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    main(N)