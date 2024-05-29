import sys

def main():
    N, M, V =map(int, sys.stdin.readline().split())
    #info = list(map(int, sys.stdin.readline().split()))
    #N = int(sys.stdin.readline())
    #print(N,M,V)
    #ans = []
    #ans.append(V)
    graph = [[] for _ in range(N+1)] #{}
    #for i in range(N):
    #    graph[i+1] = []
    for i in range(M):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        #graph[a].sort()
        #graph[b].sort()
    for i in range(N):
        graph[i+1].sort()
    
    #print(graph)
    print(*dfs2(graph,V))
    print(*bfs(graph, V))
    #for item in dfs2(graph,V):
    #    print(item, end=' ')
    #print()
    #print(dfs2(graph, V))
    #for item in bfs(graph, V):
    #    print(item, end=' ')



def dfs1(graph, v, visited): #재귀함수로 짜보자
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs1(graph, i, visited)


def dfs2(graph, v): #스택(list)으로 짜보자
    answer = []
    visited = [False] * (len(graph)+1)
    stack = []
    stack.append(v)
    
    while stack:#.empty():
        a = stack.pop()
        #print(a, end='')
        answer.append(a)
        visited[a] = True
        for i in reversed(graph[a]):  #이거 역순reversed()으로 들어가야 함/ 아님/ 맞음
            if not visited[i]:    
                if i in stack:
                    stack.remove(i)
                stack.append(i)
                    #break
    return answer  

    #visited[v] = True
    #print(v, end='')

from collections import deque

def bfs(graph, start):
    answer=[]
    visited = [False] * (len(graph)+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        #print(v, end='')
        answer.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return answer
if __name__ == "__main__":
    main()