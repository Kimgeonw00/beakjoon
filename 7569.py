import sys
from collections import deque
import copy

def main():
    N, M, H =map(int, sys.stdin.readline().split())
    total_graph = []
    for _ in range(H):
        floor = [] 
        for _ in range(M):
            floor.append(list(map(int, sys.stdin.readline().split())))
            #print(floor)
            #floor.append(list(map(int, sys.stdin.readline().split()))) #input())))#sys.stdin.readline())))
            #sys.stdin.readline().split()
        total_graph.append(floor)
    sub_graph = copy.deepcopy(total_graph)
    #print(total_graph)
    #visited = [[[False]*N for _ in range(M)] for _ in range(H)] # x, y, z
    #print(visited)
    #for item in range(len(total_graph)):
    #    for jtem in range(len(item)):
    #        for k in range(len(jtem)):
    #            if jtem[k]==1

    #movement = [(-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    #q = deque()
    #q.append((0,0,0,0)) #(x,y,z,cost)
    #a=0
    """while q:
        if a>0:
            break
        nx, ny, nz, cost = q.popleft()
        for dx, dy, dz in movement:
            x = nx + dx
            y = ny + dy
            z = nz + dz
            if (0<=x<N) and (0<=y<M) and (0<=z<H) and total_graph[z][y][x] != -1 and not visited[z][y][x]:
                if total_graph[z][y][x]==1:
                    print(cost+1)
                    #goto exit
                    a+=1
                    break
                else:
                    visited[z][y][x] = True
                    q.append((x,y,z,cost+1))"""
    answer = [0]
    for k in range(H):
        for j in range(M):
            for i in range(N):
                if sub_graph[k][j][i]==0:
                    ans, sub_graph = find_one(total_graph,(i,j,k), sub_graph)
                    answer.append(ans)
    if -1 in answer:
        print(-1)
    else:
        print(max(answer))

def find_one(total_graph, start, sub_graph):
    h = len(total_graph)
    m = len(total_graph[0])
    n = len(total_graph[0][0])
    visited = [[[False]*n for _ in range(m)] for _ in range(h)]
    movement = [(-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    x,y,z = start
    q = deque()
    q.append((x,y,z,0))
    while q:
        nx, ny, nz, cost = q.popleft()
        if total_graph[nz][ny][nx]!=0:
            return 0, sub_graph
        for dx, dy, dz in movement:
            x = nx + dx
            y = ny + dy
            z = nz + dz
            if (0<=x<n) and (0<=y<m) and (0<=z<h) and total_graph[z][y][x] != -1 and not visited[z][y][x]:
                if total_graph[z][y][x]==1:
                    return cost+1, sub_graph
                else:
                    visited[z][y][x] = True
                    sub_graph[z][y][x] = -1
                    q.append((x,y,z,cost+1))
    return -1, sub_graph


def main2():
    N, M, H =map(int, sys.stdin.readline().split())
    total_graph = []
    for _ in range(H):
        floor = [] 
        for _ in range(M):
            floor.append(list(map(int, sys.stdin.readline().split())))
        total_graph.append(floor) 
    visited = [[[False]*N for _ in range(M)] for _ in range(H)]
    movement = [(-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

    # 그래프를 돌며 1이 있는 곳의 좌표를 큐에 넣자.
    q = deque()
    answer = []
    for k in range(H):
        for j in range(M):
            for i in range(N):
                if total_graph[k][j][i]!=0:
                    if total_graph[k][j][i]==1:
                        visited[k][j][i]=True
                        q.append((i,j,k,0))
                        answer.append(0)
                    else:
                        visited[k][j][i]=True
                        answer.append(0)
    while q:
        nx, ny, nz, cost = q.popleft()
        for dx, dy, dz in movement:
            x = nx + dx
            y = ny + dy
            z = nz + dz
            if (0<=x<N) and (0<=y<M) and (0<=z<H) and total_graph[z][y][x] == 0 and not visited[z][y][x]:
                visited[z][y][x] = True
                q.append((x,y,z,cost+1))
                answer.append(cost+1)
    #모든 곳에 방문했다
    if len(answer)< N*M*H:
        print(-1)
    else:
        print(max(answer))
if __name__ == "__main__":
    main2()