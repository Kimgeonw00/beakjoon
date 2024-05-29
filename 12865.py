import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    box = []
    box.append([0,0])
    for _ in range(N):
        W, V = map(int, sys.stdin.readline().split())
        box.append([W,V])
    #print(bag(item, K, 0))
    bag = [[0,K]] # 첫 행에는 value, 남은 자리
    
    dp_table = [[0 for _ in range(N+1)] for _ in range(K+1)]
    #print(dp_table)
    #print(dp_table[K][N-1])

    for j in range(N+1): #j는 아이템 순번
        for i in range(K+1): #i는 가방 무게
            w, v = box[j]
            if w>i: #무거우면
                dp_table[i][j] = dp_table[i][j-1]
            else:  #가벼우면 넣거나 안넣거나?
                dp_table[i][j] = max(v + dp_table[i-w][j-1], dp_table[i][j-1])
    print(dp_table[-1][-1])
#너무 브루트포스로 풀어서 시간이 오래 걸리는 듯 하다.
"""def bag(item, left_k, value):
    if len(item)>1:
        w, v = item[0]
        if w > left_k: #무거워서 못넣음
            return bag(item[1:], left_k, value)
        else: #넣을 수 있음
            return max(bag(item[1:], left_k-w, value+v), bag(item[1:], left_k, value))
    else:
        w, v = item[0]
        if w > left_k: #못넣음
            return value
        else: #넣음
            return value + v"""




if __name__ == "__main__":
    main()