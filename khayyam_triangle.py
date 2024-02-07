def khayyam(m,n) :
    l = []
    for i in range(m+1) :
        l1 = []
        for j in range(i+1) :
            if i==j or j==0 :
                l1.append(1)
            else :
                l1.append(l[i-1][j]+l[i-1][j-1])
        l.append(l1)
    return l[m][n]


def main() :
    m, n = map(int,input("please enter a,b in (a choose b) : ").split())
    print(khayyam(m,n))


if __name__ == "__main__" :
    main()
