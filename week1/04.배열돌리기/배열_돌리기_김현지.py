def rotate(n, d, array):
    rotationCnt = (d // 45) % 8

    for _ in range(rotationCnt):
        mainDiag = [array[i][i] for i in range(n)]
        midCol =[array[i][n//2] for i in range(n)]
        subDiag = [array[i][n-1-i] for i in range(n)]
        midRow = [array[n//2][i] for i in range(n)]

        ### 안되는 이유:
        ## 배열의 일부를 다른 위치에 직접 대입하려고 할 때,
        ## 한 위치의 참조를 다른 변수에 할당
        ## 결론: 다른 위치에서 같은 데이터 가리키게 됨
        ## 해결: 단순 '복사'가 아닌 '복사'하여 새 위치에 '할당' 필요

        # midCol = mainDiag
        # subDiag = midCol
        # midRow = subDiag
        # mainDiag = midRow
        for i in range(n):
            array[i][n//2] = mainDiag[i]
            array[i][n-1-i] = midCol[i]
            array[n//2][n-1-i] = subDiag[i]
            array[i][i] = midRow[i]


    for row in array:
        print(" ".join(map(str, row)))


T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    rotate(n, d, array)

