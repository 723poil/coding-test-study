"""
Quick Sort 알고리즘에서 투포인터와 유사한 방식을 사용 => partition
Quick Sort는 시간복잡도가 O(nlogn)

- partiiton을 재귀로 반복
- 반복하면서 맨 오른쪽에 있는 값(pivot)을 제자리에 두기
- 주의! quick_sort에서 pivot을 포함해서 partition을 정렬하면, 무한 루프에 빠짐
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 # pivot보다 작은 마지막 index
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1            


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

nm_list = n_list + m_list
quick_sort(nm_list, 0, len(nm_list)-1)

print(nm_list)