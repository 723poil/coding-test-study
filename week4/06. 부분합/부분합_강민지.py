"""
*** 결과: 시간 초과 => 이중 for문 불가 => 투포인터 while문 사용하기 ***
* 투포인터가 같은 방향으로 이동 (왼->오)
* 종료조건 : right이 seq를 넘길 때

1. 부분합이 s 이상
    - answer에 저장
    - left + 1

2. 부분합이 s 미만
    - right + 1 (만약 seq를 넘기면 break)

sum을 계속 seq로 더하면 시간초과 나옴
sum을 정해놓고 주어진 index에 해당하는 값을 더하고 빼야함
"""
import sys
input = sys.stdin.readline

def main(n, s, seq):
    
    left, right = 0, 0
    answer = int(1e6)
    subseq_sum = 0
    
    while 1:
        # 부분합 >= s
        if subseq_sum >= s:
            answer = min(right-left, answer)
            subseq_sum -= seq[left] # 이동하기 전에 빼기!
            left += 1

        elif right >= n: # 이 조건을 따로 빼는 것이 관건
            break

        # 부분합 < s
        else:
            subseq_sum += seq[right]
            right += 1

    if answer == int(1e6):
        return 0
    return answer

if __name__ == "__main__":
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    print(main(n, s, seq))

