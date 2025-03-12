def linear_search(A,n,key):
    i=0#index
    while i<n:#n is length of array
        if A[i]==key:
            return i
        i=i+1
    return -1

A=[8,5,2,3,9,7]
n=len(A)
key=7
print(linear_search(A,n,key))