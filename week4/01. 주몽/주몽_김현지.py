def solution():
    left, right = 0, len(ingredients)-1
    cnt = 0
    while left < right:
        currentSum = ingredients[left] + ingredients[right]
        if currentSum < M:
            left += 1
        elif currentSum > M:
            right -= 1
        elif currentSum == M:
            cnt += 1
            left += 1
            right -= 1
    return cnt

N = int(input()) # 재료의 개수
M = int(input()) # 갑옷을 만드는데 필요한 수
ingredients = list(map(int, input().split())) # 재료 번호
ingredients.sort()
print(solution())
