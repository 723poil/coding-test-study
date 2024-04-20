from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

input = stdin.readline


def postorder(start, end):
    if start >= end:
        print(tree_list[start])
        return
    
    if tree_list[start] > tree_list[end] or tree_list[start] < tree_list[start + 1]:
        postorder(start+1, end)
        print(tree_list[start])
        return
    
    mid = 0
    
    for i in range(start + 1, end + 1):
        if tree_list[start] < tree_list[i]:
            mid = i
            break
    
    postorder(start+1, mid - 1)
    postorder(mid, end)
    print(tree_list[start])


if __name__ == '__main__':
    
    tree_list = []
    
    n = input()
    while n:
        tree_list.append(int(n))
        n = input()
        
    postorder(0, len(tree_list) - 1)