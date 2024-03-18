# # 문제 이해 - 요구사항 정리 - 패턴 분석 - 구현 - 예외 케이스

import sys
num_bulb, num_command = map(int, sys.stdin.readline().split()) 
bulb_list = list(map(int, sys.stdin.readline().split())) 
# command_list = list(map(int, sys.stdin.readline().split()))

command_mat = [list(map(int, sys.stdin.readline().split())) for _ in range(num_command)]

# print(command_mat)
# 1번째 명령 실행 함수
def cmd_1(bulb_list, command_list):
    if bulb_list[command_list[1]] == 0:
        bulb_list[command_list[1]] += 1
    else:
        bulb_list[command_list[1]] -= 1
    
    return bulb_list

# # 2번째 명령 실행 함수
# def cmd_2(bulb_list, command_idx):
#     pass

# # 3번째 명령 실행 함수
# def cmd_3(bulb_list, command_idx):
#     pass

# # 4번째 명령 실행 함수
# def cmd_4(bulb_list, command_idx):
#     pass    

def main(num_bulb, num_command, bulb_list, command_mat):
    # for command_list in command_mat:
    for command_list in command_mat:
        # 1번째 명령
        if command_list[0] == 1:
            bulb_list = cmd_1(bulb_list, command_list)
        elif command_list[0] == 2:
            pass    
        elif command_list[0] == 3:
            pass
        else:
            pass
    # print(command_mat)
    return bulb_list

main(num_bulb, num_command, bulb_list, command_mat)