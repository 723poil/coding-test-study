"""
*** 결과 : 틀렸습니다
* 반례 - 사용할 제품 뒤쪽에 반복되는 제품이 있는 경우 주의
* 쉽게 푼 풀이 => https://magentino.tistory.com/88
"""


def select_product(sockets, order_list, i):
    """i번째 제품을 사용하려고 할 때, 플러그를 뽑을 제품 선택하기"""
    order_backward_list = order_list[i+1:]
    selected_idx = 0
    for s in sockets:
        if s not in order_backward_list:
            return s
        for j in range(i+1, len(order_list)):
            if s == order_list[j]:
                selected_idx = max(j, selected_idx)
                break
    return order_list[selected_idx] if selected_idx else 0


if __name__=="__main__":

    n, k = map(int, input().split())
    order_list = list(map(int, input().split()))


    answer = 0
    sockets = []

    for i in range(k):

        # i 제품이 꽂혀있지 않은 경우 => 1) 꽂기 or 2) 뺐다 꽂기
        product = order_list[i]
        # print(f"--> {i}th prods ({product})")
        if product not in sockets:
            ## 1) 꽂기
            if len(sockets) < n:
                sockets.append(product)
            ## 2) 뺐다 꽂기
            elif i==k-1: # 마지막으로 사용하는 제품 => 어떤 걸 빼도 상관없음
                answer += 1
            else: # 어떤 걸 뺄까? => 이후 사용 계획이 없거나 제일 뒤 쪽에 등장하는 제품
                rm_prod = select_product(sockets, order_list, i)
                rm_prod = rm_prod if rm_prod else sockets[0]
                sockets.remove(rm_prod)
                answer += 1
                sockets.append(order_list[i])
                
        # print(f"==> sockets: {sockets}")
        # print(f"*** answer: {answer}")
        # print()
    print(answer)
