"""
* 배달해야 하는 봉지 수 => list로 저장
"""


n = int(input())

bag_nums = [5000] * 5001

bag_nums[3] = bag_nums[5] = 1 # immutable object만 가능(숫자, 문자, 튜플)


for i in range(6, n+1):
    bag_nums[i] = min(bag_nums[i-3], bag_nums[i-5]) + 1
    
bag = bag_nums[n]

if bag >= 5000:
    print(-1)
else:
    print(bag)