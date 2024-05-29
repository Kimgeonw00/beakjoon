import sys

def find_opt(arr, target):
    arr.reverse()
    idx = arr.index(target)
    if idx+1 == len(arr):
        del arr[idx]
        arr.reverse()
        return arr
    for i in range(idx+1, len(arr)):
        a = 0
        if arr[i]==target:
            if arr[i-1]>arr[i]:
                a = i
    if a!=0:
        idx = a
    del arr[idx]
    arr.reverse()
    
    return arr

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    origin = [int(digit) for digit in str(a)]
    minus = [int(digit) for digit in str(b)]
    minus.sort()
    for item in minus:
        origin = find_opt(origin, item)
    num = int(''.join(map(str, origin)))
    print(num)


def main2():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    origin = [int(digit) for digit in str(a)]
    minus = [int(digit) for digit in str(b)]
    minus.sort()
    for item in minus:
        origin = find_opt(origin, item)
    
    num = int(''.join(map(str, origin)))
    print(num)
if __name__ == "__main__":
    main()