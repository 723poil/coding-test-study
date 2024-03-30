def rotate_clockwise(arr):
    n = len(arr)
    new_arr = [i.copy() for i in arr]
    mid_idx = int((n+1)/2)-1
    
    for i in range(n):
        # 1) 주 -> 열 
        new_arr[i][mid_idx] = arr[i][i]
        # 2) 열 -> 부
        new_arr[i][n-1-i] = arr[i][mid_idx]
        # 3) 부 -> 행
        new_arr[mid_idx][i] = arr[n-1-i][i]
        # 4) 행 -> 주
        new_arr[i][i] = arr[mid_idx][i]

    return new_arr

def rotate_anti_clockwise(arr):
    n = len(arr)
    new_arr = [i.copy() for i in arr]
    mid_idx = int((n+1)/2)-1

    for i in range(n):
        # 1) 열 -> 주
        new_arr[i][i] = arr[i][mid_idx]
        # 2) 부 -> 열
        new_arr[i][mid_idx] = arr[i][n-1-i]
        # 3) 행 -> 부
        new_arr[n-1-i][i] = arr[mid_idx][i]
        # 4) 주 -> 행
        new_arr[mid_idx][i] = arr[i][i]
    return new_arr

def main(angle, arr):

    rotate_cnt = int(angle/45)
    is_clockwise = rotate_cnt >= 0 
    
    if is_clockwise:
        for _ in range(rotate_cnt):
            arr = rotate_clockwise(arr)

    else:
        for _ in range(-rotate_cnt):
            arr = rotate_anti_clockwise(arr)

    return arr

if __name__ == "__main__":
    
    T = int(input()) # test case nums
    
    test_case_list = []
    for _ in range(T):
        n, angle = map(int, input().split())
        arr = [list(map(int, input().split())) for i in range(n)]
        test_case_list.append((angle, arr))
    
    for test_case in test_case_list:
        angle, arr = test_case
        answer = main(angle, arr)
        for a_list in answer:
            print(' '.join(map(str, a_list)))