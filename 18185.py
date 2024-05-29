import sys

def buy1(ind, A,k):
    A[ind]-=k
    #cost+=3
    #print(cost)

def buy2(ind, A,k):
    A[ind]-=k
    A[ind+1]-=k
    #cost+=5

def buy3(ind, A,k):
    A[ind]-=k
    A[ind+1]-=k
    A[ind+2]-=k
    #cost+=7

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))+[0,0]
    #print(N)
    cost = 0

    for idx in range(N):
        if A[idx+1]>A[idx+2]:
            m = min(A[idx], A[idx+1]-A[idx+2])
            buy2(idx, A, m)
            cost+=m*5
        n = min(A[idx], A[idx+1])
        buy3(idx, A, n)
        cost+=n*7
        l = A[idx]
        buy1(idx, A, A[idx])
        cost+=l*3
    
    print(cost)
if __name__ == "__main__":
    main()