"""
round 작동 방식이 특이해서 문자 포매팅을 사용해야 정답이 됨
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

tree_dict = defaultdict(int)
total = 0
while True:
    tree = input().rstrip()
    if not tree:
        break

    tree_dict[tree] += 1
    total += 1

for tree in sorted(tree_dict):
    print("{} {:.4f}".format(tree, tree_dict[tree]/total*100))