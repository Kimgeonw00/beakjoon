import sys

def main():
    N = int(sys.stdin.readline())
    T=[]
    P=[]
    for i in range(N):
        t , p = map(int, sys.stdin.readline().split())
        T.append(t)
        P.append(p)    
    #print(T, P)
    print(poten(T,P))

#가능한 날짜조합을 모두 구한 후, max를 출력

def poten(T,P):
    if len(T)==1:
        if T[0]==1:
            return P[0]
        else:
            return 0
    if T[0]>len(T):
        return poten(T[1:],P[1:])
    elif T[0]==len(T):
        return max(P[0], poten(T[1:],P[1:]))
    else:
        return max(poten(T[1:],P[1:]), 
                   P[0]+ poten(T[T[0]:], P[T[0]: ]))


if __name__ =="__main__":
    main()