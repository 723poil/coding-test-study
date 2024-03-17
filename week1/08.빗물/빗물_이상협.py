from sys import stdin

input = stdin.readline

blocks = []
count = 0

def check_water(start, end):
    global blocks, count
    
    if end - start <= 1:
        return
    
    min_block = min(blocks[start], blocks[end])
    if end - start >= 2:
        max_block = max(blocks[start+1: end])
    
        if max_block >= min(blocks[start], blocks[end]):
            middle = blocks[start+1: end].index(max_block)
            
            check_water(start, middle + start + 1)
            check_water(middle + start + 1, end)
            return
        
    if start == 0 and blocks[start] == 0:
        return
    
    if end == len(blocks) -1 and blocks[end] == 0:
        return
        
    for block in blocks[start+1: end]:
        count += (min_block - block)


def solution():
    global blocks
    
    H, W = map(int, input().split())
    
    blocks = list(map(int, input().split()))
    
    check_water(0, W - 1)

solution()

print(count)