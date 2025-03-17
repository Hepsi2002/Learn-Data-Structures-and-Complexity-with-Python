def bubblesort(A):
    n=len(A)
    for passes in range(n-1,0,-1):
        for i in range(0,passes):
            if A[i]>A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
            


A=[47,5,57,56,13,15,63,85,4,52,32,59]
bubblesort(A)
print(A)