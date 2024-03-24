def create_distsum(m):
    """분해합 구하는 함수"""
    r = m
    answer = 0

    while r > 0:
        answer += r % 10
        r = r // 10
    
    answer += m
    return answer


def main(n):
    k = len(str(n)) - 1
    m = 10**(k-1) if k>=1 else 1

    for i in range(m, n):
        distsum = create_distsum(i)
        if distsum == n:
            return i
    return 0


n = int(input())
print(main(n))