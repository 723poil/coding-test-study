def solution():
    left, right = 0, 0
    minLength = MAX
    currentSum = sequences[0]
    while right < len(sequences):
        if currentSum < S:
            right += 1
            if right > len(sequences)-1:
                break
            currentSum += sequences[right]
        elif currentSum >= S:
            minLength = min(minLength, right - left + 1)
            currentSum -= sequences[left]
            left += 1
    return minLength

N, S = map(int, input().split())
sequences = list(map(int, input().split(" ")))
MAX = int(1e9)
minLengthSol = solution()
print(minLengthSol if minLengthSol != MAX else 0)

