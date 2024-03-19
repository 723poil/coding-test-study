import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 전구의 갯수는 n이다. string으로 묶고 int랑 어쩌고 해서 비트 연산을 통해서 reverse한다.

lst = list(map(int, input().split()))

for i in range(m):
    a, b, c = map(int , input().split())
    if a == 1: # 비트 연산자를 통해서 반전
        lst[b-1] = c
    elif a == 2: # 비트 연산자를 통해서 다 reverse
        for j in range(b-1, c):
            if lst[j] == 0:
                lst[j] = 1
            else:
                lst[j] = 0
    elif a == 3:
        for j in range(b-1, c):
            if lst[j] == 1:
                lst[j] = 0
    else:
        for j in range(b-1, c):
            if lst[j] == 0:
                lst[j] = 1
print(*lst)
