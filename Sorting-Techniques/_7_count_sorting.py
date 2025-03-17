def countsort(A):
    n=len(A)
    maxsize=max(A)
    count_array = [0]* (maxsize+1)
    for i in range(n):
        count_array[A[i]]=count_array[A[i]]+1
    i,j=0,0
    while i<maxsize+1:
        if count_array[i]>0:
            A[j]=i
            j=j+1
            count_array[i]=count_array[i]-1
        else:
            i=i+1

A=[3,5,8,9,6,2,3,5,5]
countsort(A)
print(A)
