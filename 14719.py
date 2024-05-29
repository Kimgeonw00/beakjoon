import sys

def main():
    H, W = map(int, sys.stdin.readline().split())
    block = list(map(int, sys.stdin.readline().split()))
    rain = 0
    wall = [0,0] #높이, 좌표
    for i in range(W-1):
        if block[i]>=wall[0]:#더 높은 벽이 나타나면
            if i-wall[1]-1<=0:
                rain+=0
            else:
                plus = (i-wall[1]-1)*wall[0]-sum(block[wall[1]+1:i])
                rain += plus
            wall = [block[i],i]
    #마지막인 경우 conner case를 고려
    if block[-1]>=wall[0]:
        plus = ((W-1)-wall[1]-1)*wall[0]-sum(block[wall[1]+1:W-1])
        rain += plus
    else:
        plus = ((W-1)-wall[1]-1)*block[-1]-sum(block[wall[1]+1:W-1])
        rain += plus
    
    print(rain)

def main2():
    H, W = map(int, sys.stdin.readline().split())
    block = list(map(int, sys.stdin.readline().split()))
    block.append(0)
    rain = 0
    wall = []
    invi = 0
    for i in range(W):
        if i == 0:
            wall.append(block[i])
        if block[i] <= block[i-1]: #더 낮아짐
            wall.append(block[i])
        else: #더 높아짐
            if block[i]>=max(wall): #최대치 갱신의 경우, 구분짓는 느낌
                #plus = max(wall)*(len(wall))-sum(wall) 
                #rain += plus
                most = max(wall)
                for item in wall:
                    if item < most:
                        rain += (most - item)
                invi = 0
                wall = [block[i]]
            else: #높아지긴 했는데 그정돈 아님
                if block[i]>block[i+1]: #높아졌다 낮아질 거임
                    for item in reversed(wall):
                        if item < block[i]:
                            invi += block[i]-item
                        else:
                            break
                wall.append(block[i])
    rain += invi
    print(rain)
if __name__ == "__main__":
    main2()