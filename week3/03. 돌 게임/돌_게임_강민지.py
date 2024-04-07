# 주의! 1개 or 3개만 가져갈 수 있음. 2개 불가능.

memo = ["", "SK", "CY", "SK"] 

def dp(n:int):
    
    global memo

    if n <= 3:
        return memo[n]

    for i in range(4, n+1):
    
        r1, r2 = i-1, i-3 

        if memo[r1] == "SK" or memo[r2] == "SK":
            memo.append("CY")
        
        else:
            memo.append("SK")

    return memo[n]
        
        
n = int(input())
print(dp(n))