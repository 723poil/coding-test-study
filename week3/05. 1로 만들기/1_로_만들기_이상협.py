from sys import stdin

input = stdin.readline

def act_dp(dp: list):
    new_dp = []
    
    for d in dp:
        new_dp.append(d - 1)
        if d % 3 == 0 and d >= 3:
            new_dp.append(d // 3)
        if d % 2 == 0 and d >= 2:
            new_dp.append(d // 2)
            
    return new_dp

def solution():
    N = int(input())
    count = 0
    
    if N == 1:
        return count
    
    dp = [N]

    while min(dp) != 1:
        dp = act_dp(dp)
        count += 1
        
    return count

print(solution())