import sys
from collections import defaultdict

input = sys.stdin.readline
trees = defaultdict(int)
totalTrees = 0
while True:
    line = input().strip()
    if not line:
        break
    trees[line] += 1
    totalTrees += 1


sortedTrees = sorted(trees.keys())

for tree in sortedTrees:
    percentage = (trees[tree] / totalTrees) * 100
    print(f"{tree} {percentage:.4f}")
