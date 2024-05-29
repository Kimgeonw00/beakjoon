import sys
    
def main():
    T = int(sys.stdin.readline())
    ans = []
    for i in range(T):
        N = int(sys.stdin.readline())
        info = list(map(int, sys.stdin.readline().split()))
        profit = 0
        while True:
            max_day = info.index(max(info))
            if max_day+1 == len(info):
                profit += len(info)*info[max_day]-sum(info)
                break
            else:
                one = info[:max_day+1]
                info = info[max_day+1:]
                profit +=len(one)*one[max_day]-sum(one)
        ans.append(profit)

    for item in ans:
        print(item)
    
def main2():
    T = int(sys.stdin.readline())
    ans = []
    for i in range(T):
        N = int(sys.stdin.readline())
        info = list(map(int, sys.stdin.readline().split()))
        profit = 0
        price = 0 #보유주식의 구매 시 가격의 총합
        num = 0 #보유주식 개수
        for i in range(N-1):
            if info[i]>info[i+1]: #내일 가격이 떨어진다면? 팔아야겠죠
                profit += num*info[i] - price
                num = 0
                price = 0
            else: #내일 가격이 같거나 오른다? 사야죠
                num+=1
                price+=info[i]
        profit += num*info[-1] - price
        num = 0
        price = 0
        ans.append(profit)

    for item in ans:
        print(item)


def main3():
    T = int(sys.stdin.readline())
    ans = []
    for i in range(T):
        N = int(sys.stdin.readline())
        info = list(map(int, sys.stdin.readline().split()))
        rev_info = list(reversed(info))
        profit = 0
        max_val = 0
        for i in range(N):
            if rev_info[i]>max_val:
                max_val = rev_info[i]
            else:
                profit+=max_val-rev_info[i]
        ans.append(profit)

    for item in ans:
        print(item)

def main4():
    T = int(sys.stdin.readline())
    ans = []
    for i in range(T):
        N = int(sys.stdin.readline())
        info = list(map(int, sys.stdin.readline().split()))
        profit = 0
        max_val = 0
        for i in range(N):
            if info[N-1-i]>max_val:
                max_val = info[N-1-i]
            else:
                profit+=max_val-info[N-1-i]
        ans.append(profit)

    for item in ans:
        print(item)

if __name__ == "__main__":
    main2()