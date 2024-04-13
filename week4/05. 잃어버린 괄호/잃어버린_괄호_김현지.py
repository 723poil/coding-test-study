numbers = list(input().split('-'))
num = 0
numberCnt = len(numbers)

for i in range(numberCnt):
    if '+' in numbers[i]:
        addition = sum(list(map(int, numbers[i].split('+'))))
        if i == 0:
            num += addition
        else:
            num -= addition
    elif i == 0:
        num += int(numbers[i])
    else:
        num -= int(numbers[i])
print(num)