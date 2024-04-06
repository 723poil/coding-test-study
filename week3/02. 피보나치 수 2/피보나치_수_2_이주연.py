global lst
n=int(input())
lst=list(0 for _ in range(max(2, n+1)))
lst[0]=0
lst[1]=1

def Fibonachi(n):
    global lst
    if n == 0:
        return lst[0]
    elif n == 1:
        return lst[1]
    else:
        for i in range(2,n+1):
            lst[i]=lst[i-1]+lst[i-2]
        return lst[n]
print(Fibonachi(n))