import sys

def main():
    a = list(input())
    gop = []
    answer = 0
    while a:
        ho = a.pop()
        if ho=='(':  #'['# ]' #')' #나중에 리버스 해야되긴함
            if a[-1]=='(' or '[':
                gop.append(2)
            else:
                if a[-1] == ')':
                    a.pop()
                    val = 2
                    for item in gop:
                        val = val*item
                    answer += val
                if a[-1] == ']':
                    print(0)
                    break
        elif ho=='[':
            if a[-1]=='(' or '[':
                gop.append(3)
            else:
                if a[-1] == ']':
                    a.pop()
                    val = 3
                    for item in gop:
                        val = val*item
                    answer += val
                if a[-1] == ')':
                    print(0)
                    break

def main2():
    a = list(input())
    gop = [1]
    answer = 0
    open1=0
    open2=0
    #print(a)
    while len(a)>=2:
        ho = a.pop()
        if ho==')':  #'['# ]' #')' #나중에 리버스 해야되긴함
            open1+=1
            if a[-1]==')' or a[-1]==']':
                gop.append(2)
            else:
                if a[-1] == '(':
                    #a.pop()
                    val = 2
                    for item in gop:
                        val = val*item
                    answer += val
                if a[-1] == '[':
                    print(0)
                    exit()
        elif ho==']':
            open2+=1
            if a[-1]==')' or a[-1]==']':
                gop.append(3)
            else:
                if a[-1] == '[':
                    #a.pop()
                    val = 3
                    for item in gop:
                        val = val*item
                    answer += val
                if a[-1] == '(':
                    print(0)
                    exit()
        else:
            if ho == '(':
                open1-=1
            else:
                open2-=1
            if a[-1]=='[' or a[-1]=='(':
                if len(gop)>=2:
                    gop.pop()
                else:
                    print(0)
                    exit()

    if a[0]=='(':
        open1-=1
    elif a[0]=='[':
        open2-=1
    else:
        print(0)
        exit()
    
    if open1==0 and open2==0:
        print(answer)
    
    else:
        print(0)

if __name__ == "__main__":
    main2()