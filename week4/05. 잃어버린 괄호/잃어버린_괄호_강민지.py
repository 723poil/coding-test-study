"""
'-' 뒤에 나오는 덧셈부분에 괄호 넣기
-> '-'를 기준으로 split해서 계산하고 '-'를 맨 마지막에 계산
"""
       
def main(formula):
    split_minus = formula.split('-')

    # -를 제외한 나머지 부분을 먼저 다 계산
    parts = []
    for fm in split_minus:
        if '+' in fm:
            parts.append(sum(list(map(int, fm.split('+')))))
        else: 
            parts.append(int(fm))
    
    # 위에서 계산한 것 다 빼기
    res = parts[0]
    for p in parts[1:]:
        res -= p
    return res


formula = input()
print(main(formula))