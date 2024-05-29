import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())


    graph = [[] for _ in range(N+1)]
    into_dim = [0]*(N+1)
    
    for _ in range(M):
        x, y, k = map(int, sys.stdin.readline().split())
        graph[y].append([x,k])
        into_dim[x]+=1
    #print(graph)
    #print(into_dim)
    for i in range(1, N+1):
        if into_dim[i]==0:
            print(i, make_product(graph, i, N))
    
def make_product(graph, start, end):
    queue = deque()
    queue.append([start, 1])
    ans = 0
    while queue:
        v , num = queue.popleft()
        if  v==end:
            ans += num
        for item in graph[v]:
            i, cost = item
            queue.append([i, num*cost])
    return ans



if __name__ == "__main__":
    main()