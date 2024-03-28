"""
*** DFS Recursion Error ***
[문제]
- python의 최대 재귀 깊이 = 1000
- 만약 50x50인 경우, 모두 배추가 심어져 있다면(1이 라면) 2500번의 재귀를 수행
[해결]
- 재귀 깊이 제한 변경

*** 주의! 가로, 세로가 바뀌어 있어서 헷갈림 ***
"""

import sys
sys.setrecursionlimit(10**5)

def check_white_jirung(field, r, c):
    n, m = len(field), len(field[0])

    if r < 0 or c < 0 or r >= n or c >= m:
        return False

    exists = field[r][c]
    if exists:
        field[r][c] = 0
        check_white_jirung(field, r+1, c)
        check_white_jirung(field, r-1, c)
        check_white_jirung(field, r, c+1)
        check_white_jirung(field, r, c-1)
        return True

    return False    

def main():
    m, n, k = map(int, input().split()) # col, row, 배추 수
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        c, r = map(int, input().split())
        field[r][c] = 1

    cnt = 0
    for a in range(n):
        for b in range(m):
            if check_white_jirung(field, a, b):
                cnt += 1

    print(cnt)



if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        result = main()
