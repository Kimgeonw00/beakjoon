import sys

def main():
    N = int(sys.stdin.readline())
    ans = []
    for i in range(N):
        coin_num = 0
        choco = int(sys.stdin.readline())
        coner_case1 = [30,31,32,33,34,40,41,42,43,44]
        coner_case2 = [80,81,82,83,84,90,91,92,93,94]
        #digits = [int(digit) for digit in str(choco)]
        
        #while len(digits)>0:
        while choco>=10:
            
            max_len = len(str(choco))
            quo = choco // (10**(max_len-2)) #몫, 처음 자리수 2
            remain = choco % (10**(max_len-2)) #나머지, 뒤의 자리수


            if choco in coner_case1:
                coin = quo // 10
                coin_num +=coin
                quo = quo - coin*10
                choco = quo * (10**(max_len-2)) + remain
            if choco in coner_case2:
                choco -=50
                coin_num+=2
            else:
                if quo>=25:
                    coin = quo // 25
                    coin_num += coin
                    quo = quo - coin*25
                coin = quo // 10
                coin_num +=coin
                quo = quo - coin*10
                choco = quo * (10**(max_len-2)) + remain

        coin_num += choco
        ans.append(coin_num)


    for item in ans:
        print(item)

def main2():
    N = int(sys.stdin.readline())
    ans = []
    for i in range(N):
        coin_num = 0
        choco = int(sys.stdin.readline())
        #digits = [int(digit) for digit in str(choco)]
        
        #while len(digits)>0:
        while choco>=10:
            
            max_len = len(str(choco))
            quo = choco // (10**(max_len-2)) #몫, 처음 자리수 2
            remain = choco % (10**(max_len-2)) #나머지, 뒤의 자리수


            if quo>=25:
                coin = quo // 25
                coin_num += coin
                quo = quo - coin*25
            coin = quo // 10
            coin_num +=coin
            quo = quo - coin*10
            choco = quo * (10**(max_len-2)) + remain

        coin_num += choco
        ans.append(coin_num)


    for item in ans:
        print(item)


def main3():
    N = int(sys.stdin.readline())
    ans = []
    for i in range(N):
        coin_num = 0
        choco = int(sys.stdin.readline())
        #digits = [int(digit) for digit in str(choco)]
        
        #while len(digits)>0:
        while choco>=100:
            
            max_len = len(str(choco))
            quo = choco // (10**(max_len-2)) #몫, 처음 자리수 2
            remain = choco % (10**(max_len-2)) #나머지, 뒤의 자리수


            if quo>=25:
                coin = quo // 25
                coin_num += coin
                quo = quo - coin*25
            coin = quo // 10
            coin_num +=coin
            quo = quo - coin*10
            choco = quo * (10**(max_len-2)) + remain

        if choco>=50:
            #coin_num+=2 #25두개쓴단마인드
            #choco -=50
            choco_1 = choco
            choco_2 = choco
            coin0 = choco//10 + choco%10

            coin1 = 0
            coin2 = 0

            coin1 +=1
            choco_1-=25
            coin1 += choco_1//10 + choco_1%10
            
            coin2 +=2
            choco_2-=50
            coin2 += choco_2//10 + choco_2%10
            
            coin = min(coin0, coin1, coin2)
            coin_num+=coin

        #choco가 50 이하
        elif choco>=25:
            choco_ = choco
            coin1 = 0
            coin2 = choco//10 + choco%10
            coin1 +=1
            choco_-=25
            coin1 += choco_//10 + choco_%10
            coin = min(coin1, coin2)
            coin_num+=coin
        else:
            coin = choco//10 + choco%10
            coin_num+=coin
        #coin_num += choco
        ans.append(coin_num)


    for item in ans:
        print(item)

def under100(choco):
    if choco>=75:
        choco_1 =choco - 25
        choco_2 =choco - 50
        choco_3 =choco - 75

        coin0 = 0
        coin1 = 1
        coin2 = 2
        coin3 = 3

        coin0 += choco//10 + choco%10
        coin1 += choco_1//10 + choco_1%10
        coin2 += choco_2//10 + choco_2%10
        coin3 += choco_3//10 + choco_3%10
    
        coin = min(coin0, coin1, coin2, coin3)
    elif choco>=50:
        #coin_num+=2 #25두개쓴단마인드
        #choco -=50
        choco_1 = choco
        choco_2 = choco
        coin0 = choco//10 + choco%10

        coin1 = 0
        coin2 = 0

        coin1 +=1
        choco_1-=25
        coin1 += choco_1//10 + choco_1%10
        
        coin2 +=2
        choco_2-=50
        coin2 += choco_2//10 + choco_2%10
        
        coin = min(coin0, coin1, coin2)

    #choco가 50 이하
    elif choco>=25:
        choco_ = choco
        coin1 = 0
        coin2 = choco//10 + choco%10
        coin1 +=1
        choco_-=25
        coin1 += choco_//10 + choco_%10
        coin = min(coin1, coin2)
    else:
        coin = choco//10 + choco%10
    return coin


def main4():
    hack = [0]*100
    for i in range(100):
        hack[i] = under100(i)
    
    N = int(sys.stdin.readline())
    ans = []
    for i in range(N):
        coin_num = 0
        choco = int(sys.stdin.readline())

        
        while choco>0:
            
            max_len = int( (len(str(choco))+1)//2 * 2 )
            quo = int(choco // (10**(max_len-2))) #몫, 처음 자리수 2
            remain = int(choco % (10**(max_len-2))) #나머지, 뒤의 자리수


            coin_num += hack[quo]
            if remain<=99:
                coin_num += hack[remain]
                break

            choco = remain


        ans.append(coin_num)


    for item in ans:
        print(item)

if __name__ == "__main__":
    main4()