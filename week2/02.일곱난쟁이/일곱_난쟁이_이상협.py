from sys import stdin

input = stdin.readline

def find_two(rl: list, diff: int):
    for i in range(9):
        for j in range(9):
            if i <= j:
                continue
            
            if rl[i] + rl[j] == diff:
                return [rl[i], rl[j]]

def solution():
    
    r_list = []
    
    for _ in range(9):
        r_list.append(int(input()))
        
    rs = sum(r_list)
    
    diff = rs - 100
    
    one, two = find_two(r_list, diff)
    
    r_list.remove(one)
    r_list.remove(two)
            
    return r_list
            
result = solution()

print("\n".join(map(str, sorted(result))))