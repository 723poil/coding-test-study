def main():
    N = int(input())

    for i in range(1, N+1):
        nums = list(str(i))
        eachPositionSum = sum(map(int, nums))
        if i + eachPositionSum == N:
            return i
    return 0

generator = main()
print(generator)