# N: 배열 A의 크기, M: 배열 B의 크기
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B
result.sort()
print(" ".join(map(str, result)))
