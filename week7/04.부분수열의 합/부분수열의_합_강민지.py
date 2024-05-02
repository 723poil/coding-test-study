"""
- 틀린 이유 : 연속된 부분 수열일 필요 X
"""
def recursive(idx, curr_sum, S, seq):
    
    global answer 

    if curr_sum == S: # 이게 종료 조건이 아님. curr_sum==S에서 부분수열이 늘어날 수 있음
        answer += 1

    if idx-1 == len(seq): # 주의! 종료 조건 필요
        return
    
    for i in range(idx+1, len(seq)):
        curr_sum += seq[i]
        recursive(i, curr_sum, S, seq)
        curr_sum -= seq[i]  # backtracking


if __name__=="__main__":

    n, S = map(int, input().split())
    seq = list(map(int, input().split()))
    answer = 0

    for idx in range(n):
        recursive(idx, seq[idx], S, seq)
    print(answer)