def main():
    s = str(input())
    k = len(s)
    count = 0
    for i in range(k):
        if i==0:
            #if s[i]==0:
            count+=1
            #else:
            #    count[1]+=1
        if s[i]!=s[i-1]:
            count+=1
    count = (count-1)//2


    print(count)
if __name__ == "__main__":
    main()