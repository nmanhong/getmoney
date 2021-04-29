import random

def firstnum(fivenum,m):
    #a = random.randint(1,35)
    for i in range(m):
        if len(fivenum) == 5:
            break
        a = random.randint(1,35)
        if a not in fivenum:
            fivenum.append(a)
            #print(a)
    fivenum.sort()
    return fivenum

def secondnum(twonum,n):
    #b = random.randint(1,12)
    for i in range(n):
        if len(twonum) == 2:
            break
        b = random.randint(1,12)
        if b not in twonum:
            twonum.append(b)
            #print(b)
    twonum.sort()
    return twonum

def guessnum(nums,c,d):
    totalnum = []
    m = 10
    n = 5
    for mn in range(1,nums):
        fivenum = []
        twonum = []
        fivenum = firstnum(fivenum,m)
        twonum = secondnum(twonum,n)
        for i in range(len(fivenum)):
            totalnum.append(fivenum[i])
        for j in range(len(twonum)):
            totalnum.append(twonum[j])
    for k in range(len(totalnum)):
        if k%c == 0 and k!=0:
            print("\n")
        if k%((c * (k // c)) + d - 1) == 0 and k != 0:
            print(totalnum[k],end="  ")
            continue
        print(totalnum[k],end=" ")
        if k == len(totalnum)-1:
            print("\n")

def main():
    nums = 10
    c = 7
    d = 5
    guessnum(nums,c,d)

if __name__ == "__main__":
    main()