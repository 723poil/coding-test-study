from sys import stdin

input = stdin.readline

def preorder(p: str):
    if p != '.':
        print(p, end='')
        preorder(tree[p][0])
        preorder(tree[p][1])
        
def inorder(p: str):
    if p != '.':
        inorder(tree[p][0])
        print(p, end='')
        inorder(tree[p][1])
        
def postorder(p: str):
    if p != '.':
        postorder(tree[p][0])
        postorder(tree[p][1])
        print(p, end='')

if __name__ == '__main__':
    N = int(input())
    
    tree = dict()
    
    for _ in range(N):
        p, lc, rc = map(str, input().rstrip().split())
        
        tree[p] = [lc, rc]
        
    preorder('A')
    print()   
    inorder('A')
    print()        
    postorder('A')
    print()             