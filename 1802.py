import sys

def possible(arr):
    n= len(arr)
    D = 0
    if n==1:
        return 1
    else:
        k = int((n-1)/2)
        for idx in range(k):
            if arr[idx]==arr[n-1-idx]:
                D+=1
        if D==0:
            return possible(arr[:k])
        else:
            return 0
    
def main():
    T = int(sys.stdin.readline())
    ans = []
    for i in range(T):
        A = sys.stdin.readline().strip()

        if possible(A):
            ans.append("YES")

        else:
            ans.append("NO")

    for item in ans:
        print(item)
    
if __name__ == "__main__":
    main()