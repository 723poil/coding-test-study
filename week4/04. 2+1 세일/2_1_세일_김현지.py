N = int(input())
costs = [int(input()) for _ in range(N)]
costs.sort(reverse=True)

totalCost = 0
for i in range(N):
    if (i+1) % 3 != 0:
        totalCost += costs[i]
print(totalCost)