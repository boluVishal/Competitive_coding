def cnt (A, X, R, L):
    li = []
    l = len(A)
    l1 = len(X)
    for i in range(l1):
        count = 0
        p = A[L[i]-1:R[i]]
        for j in p:
            if(X[i] % j == 0):
                count+=1
        print(count, end =" ")
    #print(" ".join(li))

N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
L = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]

cnt(A, X, R, L)
