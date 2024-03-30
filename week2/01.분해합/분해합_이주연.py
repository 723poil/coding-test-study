def makers(n):
    i = 1
    while True:
        if i > n:
            return 0
        _sum = i
        mod = i
        while True:
            _sum += mod % 10
            mod = mod // 10
            if mod == 0:
                break
        if _sum == n:
            break
        i += 1
    return i

if __name__ == "__main__":
    n = int(input())
    print(makers(n))