def insertionsort(A):
    n=len(A)
    for i in range(1,n):
        cvalue=A[i]
        position = i
        while position>0 and cvalue<A[position-1]:#so upto 0 index the swapping can be
            # performed but when position is -1 it will stop swapping and comparing as it will be out of index
            A[position] = A[position-1]#helps in swapping the elements
            position=position -1#decrementing the positions to its left to compare the elements for sorting
        A[position] = cvalue
    return A

A=[85,45,54,75,84,58,96,32,2,24,4,12,18,26]
print(insertionsort(A))