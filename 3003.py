def main():
    A, B, C, D, E, F = map(int, input().split())
    #answer = list(map(int, input().split()))
    #target = [1,1,2,2,2,8]
    #answer = target-answer
    #for item in answer:
    a = 1-A
    b = 1-B
    c = 2-C
    d = 2-D
    e = 2-E
    f = 8-F
    print(a,b,c,d,e,f)
if __name__ == "__main__":
    main()