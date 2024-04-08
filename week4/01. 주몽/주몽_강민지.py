"""
합이 특정 값이 되는 두 원소 찾기
- 전형적인 투포인터 문제!
"""

n = int(input())
m = int(input())
mat_list = list(map(int, input().split()))
mat_list = sorted(mat_list)

left, right = 0, n-1
cnt = 0
while left < right:
    
    temp_sum = mat_list[left] + mat_list[right]

    if temp_sum == m:
        cnt += 1
        left += 1
    
    elif temp_sum < m:
        left += 1

    else:
        right -= 1
    
print(cnt)