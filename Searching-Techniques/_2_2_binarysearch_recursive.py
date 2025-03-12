def binarysearch_recursion(A,key,l,r):
    if l>r:
        return -1
    else:
        mid=(l+r)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_recursion(A,key,l,mid-1)
        elif key > A[mid]:
            return binarysearch_recursion(A,key,mid+1,r)

A=[45,54,56,67,78,87,98]#should be in sorted order
l=0
r=len(A)-1
print(binarysearch_recursion(A,78,l,r))
