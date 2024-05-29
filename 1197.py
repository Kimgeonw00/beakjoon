import sys
import heapq

def main():
    V, E = map(int, sys.stdin.readline().split())
    graph = [False]*V
    priority_queue = []
    ans = 0
    for _ in range(E):
        a, b, k = map(int, sys.stdin.readline().split())
        heapq.heappush(priority_queue, (k, [a,b]))
    #print(priority_queue)

    while False in graph:
        (k, [dot1, dot2]) = heapq.heappop(priority_queue)
        #dot1 = dot[0]
        #dot2 = dot[1]
        put = 0
        if not graph[dot1-1]:
            graph[dot1-1] = True
            put+=1
        if not graph[dot2-1]:
            graph[dot2-1] = True
            put+=1
        if put>0:
            ans+=k

    print(ans)
    #그룹화 된 채 모든 그래프가 방문 처리 될 수 있음! 방문여부보다 간선의 개수로 판단해야함


def main2():
    V, E = map(int, sys.stdin.readline().split())

    priority_queue = []
    ans = 0
    for _ in range(E):
        a, b, k = map(int, sys.stdin.readline().split())
        heapq.heappush(priority_queue, (k, [a,b]))

    """parent = [0]*(V+1)
    
    for i in range(1, V+1):
        parent[i] = i"""
    parent = [i for i in range(V + 1)]
    while priority_queue: #len(ans)<V-1:
        (k, [dot1, dot2]) = heapq.heappop(priority_queue)

        if find(parent, dot1)!=find(parent,dot2):
            ans+=k
            union(parent, dot1, dot2)
    print(ans)


def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
        #return find(parent, parent[x])
    return parent[x]

"""def union(parent, a,b):
    a1 = find(parent, a)
    b1 = find(parent, b)
    if a1<b1:
        parent[b1] = a1
    else:
        parent[a1] = b1"""
def union(parent, a,b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA!=rootB:
        parent[rootB] = rootA

if __name__ == "__main__":
    main2()