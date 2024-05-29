import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    use = list(map(int,sys.stdin.readline().split()))
    ans = 0
    plug = []
    for i in range(len(use)):
        if use[i] in plug: #이미 꽂혀 있다면
            pass
        else:
            if len(plug)<N: #자리가 있으면
                plug.append(use[i])
            else: #새로 꽂아야하는데 자리가 없는 경우, 하나를 빼야하는데 뭐를 뺄것인가
                return 0
                
# 1 2 3 4 5 1 3 4
# 124
#3번

def main2():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    N = data[0]  # 멀티탭 구멍 수
    K = data[1]  # 전기 제품 사용 총 횟수
    use_order = data[2:]  # 전기 제품 사용 순서
    
    # 현재 멀티탭 상태 (멀티탭에 꽂혀있는 전기 제품)
    current_plugs = []
    unplug_count = 0
    
    for i in range(K):
        current_device = use_order[i]
        
        # 현재 전기 제품이 이미 꽂혀 있으면 넘어감
        if current_device in current_plugs:
            continue
        
        # 멀티탭에 빈 자리가 있으면 꽂음
        if len(current_plugs) < N:
            current_plugs.append(current_device)
            continue
        
        # 꽂혀 있는 전기 제품 중 하나를 빼야 함
        farthest_idx = -1
        plug_to_unplug = -1
        
        for plug in current_plugs:
            # 현재 전기 제품이 이후에 사용되지 않는 경우
            if plug not in use_order[i:]:
                plug_to_unplug = plug
                break
            
            # 가장 나중에 사용되는 전기 제품 찾기
            next_use_idx = use_order[i:].index(plug) #현재 사용중인 제품(plug) 가 얼마 후에 쓰이는가
            if next_use_idx > farthest_idx: #더 뒤에 쓰이는 놈
                farthest_idx = next_use_idx #으로 바꿈
                plug_to_unplug = plug
        
        # 해당 전기 제품을 멀티탭에서 뺌
        current_plugs.remove(plug_to_unplug)
        current_plugs.append(current_device)
        unplug_count += 1
    
    print(unplug_count)

if __name__ == "__main__":
    main2()



