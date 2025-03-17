def selectionsort(A):
    n=len(A)
    for i in range(0,n-1):
        position=i
        for j in range(i+1,n):
            if A[j]<A[position]:
                position=j
        temp=A[i]
        A[i]=A[position]
        A[position]=temp
    return A

#A=list(map(int, input("Enter numbers: ").split()))
A= [int(x) for x in input("Enter numbers: ").split()]
print(selectionsort(A))
"""
Time complexity for selection sort is O(n^2)
since for loop 'i' runs for n times and also 'j'
"""

