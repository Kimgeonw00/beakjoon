import sys
    
def main():
    N = int(sys.stdin.readline())
    answer = 0
    ans = [0,0]
    for i in range(N):
        card = int(sys.stdin.readline())
        if i==0 or i==1:
            ans[i]=card
        else:
            ans.append(card)
            ans.sort()
            answer +=ans[0]+ans[1]
            ans = [ans[0]+ans[1], ans[2]]
            #answer += ans[0]
    answer += ans[0]+ans[1]
    print(answer)

import heapq
def main2():
    N = int(sys.stdin.readline())
    answer = 0
    dec = []
    for i in range(N):
        card = int(sys.stdin.readline())
        dec.append(card)
    heapq.heapify(dec)

    while len(dec)!=1:
        first = heapq.heappop(dec)
        second = heapq.heappop(dec)
        res = first + second
        answer +=res
        heapq.heappush(dec, res)

    print(answer)

if __name__ == "__main__":
    main2()