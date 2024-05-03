"""
1. 모든 comb 구해서 가능여부 확인
2. backtracking (pick!)
"""

def get_remove_queens(target, n):
    drdc = [(1, -1), (1, 0), (1, 1),
            (0, -1), (0, 0), (0, 1),
            (-1, -1), (-1, 0), (-1, 1)]
    
    remove_q = []
    for dr, dc in drdc:
        new_target = (target[0]+dr, target[1]+dc)
        if 0 <= target[0]+dr < n and 0 <= target[1]+dc < n:
            remove_q.append(new_target)
    
    return remove_q


def recursive(curr, remain_q_list, q_on_board):

    global answer, n

    # 종료 조건1 : 말이 다 놓인 경우
    if len(q_on_board) == n:
        answer += 1
        print(q_on_board)
        return
    
    # 종료 조건2 : 남은 자리가 없는 경우
    if remain_q_list == []:
        return
    
    # 말을 더 놓아야 하는 경우
        ## curr 주변 자리 제거
    rm_q = get_remove_queens(curr, n)
    # print(f"curr({curr}) -> rm_q : {rm_q}")
    remain_q_list = [i for i in remain_q_list if i not in rm_q]
    # print(f"remain_q_list: {remain_q_list}")

        ## 새로운 말 추가 (주어진 말의 뒤쪽 말만 보기)
    for i in range(len(remain_q_list)):
        q = remain_q_list[i]
        q_on_board.append(q)
        recursive(q, remain_q_list[i+1:], q_on_board)
        q_on_board.pop() # backtracking
        


n = int(input())
remains = [(i, j) for i in range(n) for j in range(n)]
answer=0

for i in range(n**2-2*n):
    curr = remains[i]
    remain_q_list = remains[i:]
    recursive(curr, remain_q_list, [curr])

print(answer)