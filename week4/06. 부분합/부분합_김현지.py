def solution():
    left, right = 0, 0
    minLength = MAX
    currentSum = sequences[0]
    # print("minLength", minLength, "currentSum", currentSum)
    while right < len(sequences):
        # print("minLength", minLength, "currentSum", currentSum, "left", left, "right", right)
        if currentSum < S:
            right += 1
            if right > len(sequences)-1:
                break
            currentSum += sequences[right]
        elif currentSum > S:
            currentSum -= sequences[left]
            left += 1
        elif currentSum == S:
            minLength = min(minLength, right - left + 1)
            right += 1
            currentSum += sequences[right]
    return minLength

N, S = map(int, input().split())
sequences = list(map(int, input().split(" ")))
MAX = int(1e9)
minLengthSol = solution()
print(minLengthSol if minLengthSol != MAX else 0)

