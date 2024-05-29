import sys

def main():
    T = int(sys.stdin.readline())
    final = []
    A=[]
    B=[]
    for i in range(T):
        ans = []
        #A = sys.stdin.readline().strip()
        new = list(map(int, sys.stdin.readline().split()))
        A.append(int(new[0]))
        B.append(int(new[1]))
        for j in A:
            C = [x + j for x in B] #리스트 컴프리헨션
            ans.append(max(C))
        final.append(min(ans))
    
    for item in final:
        print(item)

def main2():
    T = int(sys.stdin.readline())
    final = []
    A=[]
    B=[]
    for i in range(T):
        ans = []
        #A = sys.stdin.readline().strip()
        new = list(map(int, sys.stdin.readline().split()))
        A.append(int(new[0]))
        B.append(int(new[1]))
        A.sort()
        B.sort(reverse=True)
        for j in range(len(A)):
            ans.append(A[j]+B[j])
        final.append(max(ans))
    
    for item in final:
        print(item)

def main3():  #input 숫자의 범위가 100이내인 점을 이용해보자!
    T = int(sys.stdin.readline())
    final = []
    A=[0]*100
    B=[0]*100
    for i in range(T):
        ans = []
        #A = sys.stdin.readline().strip()
        new = list(map(int, sys.stdin.readline().split()))
        A[new[0]-1]+=1
        B[new[1]-1]+=1
        
        useA = A[:]
        useB = B[:]
        N = sum(A)
        upper = 0
        down = 99
        max_val = 0
        for j in range(N):
            while useA[upper]==0:
                upper+=1
            while useB[down]==0:
                down-=1
            c = upper+1+down+1
            useA[upper]-=1
            useB[down]-=1
            if c> max_val:
                max_val = c
        final.append(max_val)

    for item in final:
        print(item)

import sys

def main4():  #input 숫자의 범위가 100이내인 점을 이용해보자!
    T = int(sys.stdin.readline())
    final = []
    A=[0]*100
    B=[0]*100
    for i in range(T):
        ans = []
        l, r = map(int, sys.stdin.readline().split())
        #new = list(map(int, sys.stdin.readline().split())) #이걸 고쳐야겠네
        A[l-1]+=1
        B[r-1]+=1
        
        useA = A[:]
        useB = B[:]
        #N = sum(A) = i+1 #전체 순서쌍의 개수
        upper = 0
        down = 99
        max_val = 0
        k = 0 #소모된 쌍의 개수
        while k<i+1:
            while useA[upper]==0:
                upper+=1
            while useB[down]==0:
                down-=1
            #up_group = useA[upper]
            #down_group = useB[down]
            c = upper+1+down+1
            #useA[upper]-=1
            #useB[down]-=1
            if c> max_val:
                max_val = c
            #for _ in range(useA[upper]):
            #useB에서 up_group만큼 제외하자
            discount = min(useA[upper], useB[down])
            useA[upper] -= discount
            useB[down] -= discount
            k+=discount
        final.append(max_val)

    for item in final:
        print(item)

if __name__ == "__main__":
    main4()